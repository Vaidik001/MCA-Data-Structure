#Array is a linear data structure that stores 
# multiple elements of the same type in 
# contiguous memory locations. Each element is accessed using its index, making data retrieval very fast (Random Access).

student = ['Absent'] * 30   
rno = 16
student[rno - 1] = 'Present'
print(student)