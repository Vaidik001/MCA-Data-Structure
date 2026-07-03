"""
h2) The E-Commerce Price Filter (First occurrence ≥ target)

You’re on Flipkart. You filter products: “Show me laptops priced ₹50,000 or above.”
 Products are sorted by price. 
 Flipkart must find the first product ≥ ₹50,000 — classic binary search variant called lower bound.
"""

#Binary Search

prices = [15000, 25000, 32000, 45000, 50000, 50000, 62000, 75000]

target=int(input("Enter target price : "))
n=len(str(target))

start=0
end=len(prices)-1
ans=-1

while start<=end:
    mid=int((start+end)//2)
    
    if prices[mid]>=target:
        end=mid-1
        ans=mid
        break
    else:
        start=mid+1

if ans!=-1:
    print("First Product :", prices[ans])
    print("Index:", ans)
else:
    print("Product Not Found")