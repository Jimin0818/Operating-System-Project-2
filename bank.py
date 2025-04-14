import threading
import time
import random
from queue import Queue

# Configuration
NUM_TELLERS = 3
NUM_CUSTOMERS = 50

# Semaphores and Queues for synchronization
bank_door = threading.Semaphore(2)    # Max 2 customers can enter at once
bank_safe = threading.Semaphore(2)    # Max 2 tellers in the safe
manager = threading.Semaphore(1)      # Only 1 teller with manager at a time
teller_ready = threading.Semaphore(0) # Signals teller readiness
teller_queue = Queue()                # Queue for available tellers

# Global counters
num_customer_served = 0
num_customer_served_lock = threading.Lock()

class Teller(threading.Thread):
    def __init__(self, tid):
        super().__init__()
        self.id = tid
        self.customerAvailability = threading.Semaphore(0) # Signal from customer
        self.customer = None
        self.transaction = None

    def run(self):
        global num_customer_served
        while True:
            print(f"Teller {self.id}: Ready for Customer")
            teller_queue.put(self)
            teller_ready.release()

            self.customerAvailability.acquire()

            if self.customer is None:
                break

            print(f"Teller {self.id} [Customer {self.customer.id}]: Transaction?")
            self.transaction = self.customer.get_transaction()

            if self.transaction == "Withdraw":
                self.handle_manager_interaction()

            self.handle_safe_interaction()

            print(f"Teller {self.id} [Customer {self.customer.id}]: Transaction Complete")
            self.customer.complete.release()
            self.customer.leave.acquire()

            with num_customer_served_lock:
                num_customer_served += 1
                if num_customer_served >= NUM_CUSTOMERS:
                    break

    def handle_manager_interaction(self):
        # Teller interacts with manager
        print(f"Teller {self.id}: Going to Manager")
        manager.acquire()
        print(f"Teller {self.id}: With Manager")
        time.sleep(random.uniform(0.005, 0.03))  # Simulate time with manager
        print(f"Teller {self.id}: Manager Done")
        manager.release()

    def handle_safe_interaction(self):
        # Teller accesses safe
        print(f"Teller {self.id}: Going to Safe")
        bank_safe.acquire()
        print(f"Teller {self.id}: In Safe")
        time.sleep(random.uniform(0.01, 0.05))   # Simulate time in safe
        print(f"Teller {self.id}: Done in Safe")
        bank_safe.release()

class Customer(threading.Thread):
    def __init__(self, cid):
        super().__init__()
        self.id = cid
        self.transaction = random.choice(["Deposit", "Withdraw"])
        self.complete = threading.Semaphore(0)  # Teller signals transaction done
        self.leave = threading.Semaphore(0)     # Customer signals leaving

    def get_transaction(self):
        print(f"Customer {self.id} [Teller {self.teller.id}]: gives transaction")
        return self.transaction

    def run(self):
        time.sleep(random.uniform(0, 0.1))  # Random arrival time
        bank_door.acquire()
        print(f"Customer {self.id}: enters bank")

        teller_ready.acquire()
        teller = teller_queue.get()
        self.teller = teller
        teller.customer = self

        print(f"Customer {self.id} [Teller {teller.id}]: selects teller")
        teller.customerAvailability.release()

        self.complete.acquire()  # Wait for transaction to complete
        print(f"Customer {self.id} [Teller {teller.id}]: leaving bank")

        self.leave.release()
        bank_door.release()

# Create and start teller and customer threads
tellers_threads = [Teller(i) for i in range(NUM_TELLERS)]
customers_threads = [Customer(i) for i in range(NUM_CUSTOMERS)]

for teller in tellers_threads:
    teller.start()

for customer in customers_threads:
    customer.start()

# Wait for all customers to finish
for customer in customers_threads:
    customer.join()

# Signal tellers to terminate after all customers served
for teller in tellers_threads:
    teller.customer = None
    teller.customerAvailability.release()

for teller in tellers_threads:
    teller.join()
