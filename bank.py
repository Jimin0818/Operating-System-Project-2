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
