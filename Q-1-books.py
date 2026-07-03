'''
C1)your younger sibling is packing books into a bag. 
They don’t plan — they just look at two adjacent books, and 
if the heavier one is on top of the lighter one, they swap. 
They keep repeating this until no more swaps happen. 
Heaviest books slowly “bubble up” to the bottom.'''

#bubble sort

books = [5, 6, 3, 1, 7]

n = len(books)

for i in range(n):
    for j in range(0, n - i - 1):
        if books[j] > books[j + 1]:
            books[j], books[j + 1] = books[j + 1], books[j]

print("Books arranged in order:")
print(books)


