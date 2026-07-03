"""
c3) The Lost Student (Attendance Register)

Professor Sharma enters class and gets a call from the HOD — “Is Riya Desai present today?”
The attendance register is not sorted. Names are written in the order students sat down.
"""

#linear search

students = ["vaidik", "smit", "haresh", "mitesh", "riya"]
f = "riya"

found = False

for i in range(len(students)):
    if students[i] == f:
        print("Student found")
        found = True
        break

if found == False:
    print("Student not found")