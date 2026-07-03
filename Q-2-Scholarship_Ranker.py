"""
C2) The Scholarship Ranker
A college must give scholarships to the top 3 scorers. 
The coordinator scans the entire marksheet, finds the highest scorer, moves them to position 1. 
Then scans the remaining students for the next highest, and so on. 
Each pass = one full scan to select the minimum/maximum.
"""

#selection sort

m = [78, 92, 65, 88, 95]

n = len(m)

for i in range(n):
    big = i
    for j in range(i + 1, n):
        if m[j] > m[big]:
            big = j

    m[i], m[big] = m[big], m[i]

print("Students marks in ranking order:")
print(m)