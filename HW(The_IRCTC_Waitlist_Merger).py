"""
h3) Merge Sort — The IRCTC Waitlist Merger

IRCTC has two separately sorted waitlists — one from its mobile app,
 one from railway counters. To produce a final unified waitlist, 
 they don’t re-sort from scratch. They merge both sorted lists in one pass — compare 
 the front of each list, pick the smaller token, advance. This is exactly merge sort’s merge step.
"""


mwl=[1001,1002,1005,1008]
cwl=[1003,1004,1006,1007]
result=[]
i,j,k=0,0,0

#loop for add element with compare
while i<len(mwl) and j<len(cwl):
    if(mwl[i]<cwl[j]):
        result.append(mwl[i])
        i=i+1
    else:
        result.append(cwl[j])
        j=j+1
    k=k+1

#add remaining element 
while i<len(mwl):
    result.append(mwl[i])
    i=i+1
while j<len(cwl):
    result.append(cwl[i])
    j=j+1

print(result)






#merge sort
'''
slist1 = [2, 5, 8]
list2 = [1, 4, 7]

merged = list1 + list2

for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]

print("Merged waiting list:")
print(merged)
'''