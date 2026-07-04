#A Priority Queue is a special type of queue in 
#which elements are processed based on their priority 
# instead of only their arrival order. In this example, 
# urgent jobs are printed before normal jobs.

from collections import deque
class PrinterQueue:

    def __init__(self,max_size):
        self.urgent = deque(maxlen=max_size)
        self.normal = deque(maxlen=max_size)
        self.max_size = max_size

    def add_job(self, job, priority='normal'):
        if priority.lower() == "urgent":
            if len(self.urgent) < self.max_size:
                self.urgent.append(job)
            else:
                print("Urgent Queue is Full!")
        else:
            if len(self.normal) < self.max_size:
                self.normal.append(job)
            else:
                print("Normal Queue is Full!")

    def print_jobs(self):

        print("Printing Jobs...")

        while self.urgent:
            print("Urgent :", self.urgent.popleft())

        while self.normal:
            print("Normal :", self.normal.popleft())


# Dry run
printer = PrinterQueue(3)

# Add Jobs
printer.add_job("Report.pdf")
printer.add_job("ExamPaper.pdf", "urgent")
printer.add_job("Invoice.pdf")
printer.add_job("SalarySlip.pdf", "urgent")

# Print Jobs
printer.print_jobs()