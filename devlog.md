# Project Development Log

April 8th, 1:00 PM
Created the GitHub repository for the project. Reviewed the project rubric to understand all requirements. Set up the development environment and necessary tools.

April 10th, 8:41 PM
Created the initial bank.py file to implement Teller and Customer functionalities. Uploaded key resources to the repository, including the project instructions, an example output file, and a thread_demo reference file.

April 10th, 8:50 PM
Began implementing the core Teller and Customer classes in bank.py. Established the standardized logging format: THREAD_TYPE ID [Other_THREAD_TYPE ID]: Message.

April 10th, 9:39 PM
Developed the core structure for the Bank simulation by initializing queues, tellers, and customers according to specifications.

April 10th, 9:55 PM
Designed the operational workflow where the bank opens only after all three tellers are ready, customers cannot enter until the bank opens, each teller can serve only one customer at a time, and the bank closes automatically after all 50 customers are served.

April 10th, 10:55 PM
Completed the Teller class structure by assigning each teller a unique ID, managing teller availability and customer interactions using semaphores, simulating manager approvals and safe access with sleep, and implementing detailed standardized logging for all teller activities.

April 12th, 4:02 PM
Focused on debugging Teller functionality. Fixed initial issues related to withdrawal transactions and achieved partial functionality.

April 12th, 5:00 PM
Assessed Teller progress and confirmed that the main operations were semi-functional, with minor issues remaining.

April 12th, 5:38 PM
Finalized the primary Teller functionality, ensuring that serving customers and managing transactions worked correctly as specified.

April 13th, 1:46 PM
Started implementing the Customer class behavior.

April 13th, 2:27 PM
Completed the Customer class. Customers now enter the bank after a delay, select available tellers, complete transactions, and exit. Semaphores were used to manage entry, teller availability, and departure, with standardized messages printed for each action.

April 13th, 3:28 PM
Integrated the Teller and Customer behaviors into the full Bank simulation. Initial integration showed runtime issues that needed debugging.

April 13th, 3:50 PM
Continued debugging efforts and took a short break after encountering persistent issues.

April 13th, 6:30 PM
Finalized the README.md file, documenting project structure, simulation behavior, technologies used, and instructions for running the program.

April 13th, 7:08 PM
Resumed debugging. Resolved all syntax errors but noted that simulation behavior still required refinement to fully meet rubric standards.

April 13th, 7:32 PM
Finalized the project. Completed full debugging, ensured all functionality met rubric requirements, added clean comments throughout the code, and prepared the repository for final submission.


