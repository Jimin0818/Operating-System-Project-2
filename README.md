# Operating-System-Project-2
Project 2 for CS 4348: Operating Systems

The bank simulation involves 3 tellers and 50 customers. Customers enter the bank to perform either withdrawals or deposits, but the bank opens only when all tellers are ready. Shared resources such as the safe, manager, and bank door are controlled using semaphores. 

# Simulation Details #
Teller Behavior:
  * Announces readiness.
  * Waits for a customer to approach.
  * Asks for and receives the customer’s transaction type.
  * If it’s a withdrawal:
    * Requests manager approval (only one teller interacts with the manager at a time).
    * Simulates manager interaction with a random delay of 5–30 ms.
  * Proceeds to the safe (only two tellers allowed inside at once).
  * Simulates safe access with a random delay of 10–50 ms.
  * Completes the transaction.
  * Waits for the customer to leave.

Customer Behavior: 
  * Randomly decides to perform a deposit or withdrawal.
  * Waits 0–100 ms before entering the bank.
  * Enters the bank (only two customers allowed through the door at a time).
  * Selects an available teller or waits in line.
  * Introduces itself to the teller.
  * Communicates the transaction type.
  * Waits for the teller to complete the transaction.
  * Exits the bank.

Language: Python
Concurrency: threading.Thread, threading.Semaphore, and Queue

How to Run
Ensure Python 3.x is installed.
Run the main program file:  python bank.py
