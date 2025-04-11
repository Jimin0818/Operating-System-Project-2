import threading
import time
from queue import Queue
import random

tellers = 3
customers = 50

bank_door = threading.Semaphore(2) 
bank_safe = threading.Semaphore(2) 
manager = threading.Semaphore(1) 
teller_ready = threading.Semaphore(0) 

teller_queue = Queue()
customer_queue = Queue()

numCustomerServed = 0
numCustomerServed_lock = threading.lock()

class Teller(threading.Thread):
    def __init__(self, tid):
        super().__init__()
        self.id = tid
        self.customerAvailability = threading.Semaphore(0) # availability once taking a customer
        self.customer = None
        self.transaction = None
