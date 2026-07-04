# Definition

# An Array is a linear data structure that stores elements in contiguous memory locations. Each element is identified by its index, allowing direct access without searching.

# In this Problem

# The conveyor belt has 8 fixed slots (0–7). Each slot stores one product. The warehouse manager can:

# Check what is stored at a slot.
# Find a product.
# Update a slot.
# Check whether the conveyor belt is full.

# Since each slot has a fixed position, an Array (List) is the best choice.

belt=[""]*8

def update(index,product):
    if 0<= index and index<8:
        belt[index]=product
    else:
        print("Invalid slot!")

def check_slot(index):
    if 0<= index and index<8:
        print(f"Slot {index} : ",belt[index])
    
def find_prod(product):
    if product in belt:
        print(f"{product} found at index ",belt.index(product))
    else:   print(product," not found!")

def Check_full():
    if "" in belt:
        print("Connveyor is not full")
    else:
        print("Connveyor is full")

#Dry run...
update(0,'Laptop')
update(1,'Key Board')
update(5,'Mouse')

check_slot(1)

find_prod('Mouse')

Check_full()

print("Current conveyor Belt : ",belt)