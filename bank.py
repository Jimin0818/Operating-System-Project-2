import threading
import time
import random
from queue import Queue

tellers = 3
customers = 50

bank_door = threading.Semaphore(2) 
bank_safe = threading.Semaphore(2)  
manager = threading.Semaphore(1)    
teller_ready = threading.Semaphore(0)

teller_queue = Queue()
customer_queue = Queue()

numCustomerServed = 0
numCustomerServed_lock = threading.Lock()

class Teller(threading.Thread):
    def __init__(self, tid):
        super().__init__()
        self.id = tid
        self.customerAvailability = threading.Semaphore(0)
        self.customer = None
        self.transaction = None

    def run(self):
        global numCustomerServed
        while True:
            print(f"Teller {self.id}: Ready for Customer")
            teller_queue.put(self)
            teller_ready.release()

            self.customerAvailability.acquire()
            if self.customer is None:
                break

            print(f"Teller {self.id} [Customer {self.customer.id}]: Transaction?")
            self.transaction = self.customer.getTransaction()

            if self.transaction == "Withdraw":
                print(f"Teller {self.id}: Going to Manager")
                manager.acquire()
                print(f"Teller {self.id}: With Manager")
                time.sleep(random.uniform(0.005, 0.03))
                print(f"Teller {self.id}: Manager Done")
                manager.release()

            print(f"Teller {self.id}: Going to Safe")
            bank_safe.acquire()
            print(f"Teller {self.id}: In Safe")
            time.sleep(random.uniform(0.01, 0.05))
            print(f"Teller {self.id}: Done in Safe")
            bank_safe.release()

            print(f"Teller {self.id} [Customer {self.customer.id}]: Transaction Complete")
            self.customer.complete.release()
            self.customer.leave.acquire()

            with numCustomerServed_lock:
                numCustomerServed += 1
                if numCustomerServed >= customers:
                    break
