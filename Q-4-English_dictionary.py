"""
c4) The Dictionary Hunt

You’re in a library with a physical English dictionary. You need to find the word “Ephemeral”.
You don’t start from page 1 — you open the middle, see “M”, know E comes before M, 
so you take the left half and repeat.
"""

#binary search

dic=['Apple','Ephemeral','Ikrigay','Krishna','Yuvraj',]

#Binary Search

nm=input("Enter Book name you want to search : ")
n=len(nm)

start=0
end=len(dic)-1

while start<=end:
    print(start,end)
    mid=int((start+end)//2)
    print(dic[mid],"->",nm)
    
    if dic[mid]==nm:
        print(nm," Word found..")
        break

    if ord(dic[mid][0]) < ord(nm[0]):
        start=mid+1

    if ord(dic[mid][0]) > ord(nm[0]):
        end=mid-1
        

if start>end:
    print(nm," Word not found")