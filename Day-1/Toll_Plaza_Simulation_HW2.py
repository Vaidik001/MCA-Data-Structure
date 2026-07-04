# Definition
# A Circular Queue is a linear data structure that follows the 
# FIFO (First In, First Out) principle. In a circular queue, 
# the last position is connected to the first position, so when 
# a vehicle leaves, its empty space can be reused. This makes efficient
#  use of memory and avoids wasting empty slots.

# In this Problem
# The toll plaza has a fixed capacity of 5 vehicles. If all slots are occupied, 
# new vehicles must wait. When a vehicle exits the toll plaza, the empty slot is reused 
# by the next arriving vehicle. Therefore, a Circular Queue is the most suitable data structure.


size = 5
queue = [None] * size
front=-1
rear=-1

def enqueue(vehicle):
    global front,rear
    if (rear+1)%size==front:
        print("\nQueue is Full!")
        return
    if front==-1:
        front=0
    rear=(rear+1)%size
    queue[rear]=vehicle

    print("\nEntered vehicle is : ",vehicle,end="")

def dequeue():
    global front, rear
    if front==-1 and rear==-1:
        print("\nQueue is empty!",end="")
        return
    print("\nExited vehivle is : ",queue[front],end="")
    queue[front]=None

    if(front==rear):
        front=rear=-1
    else:
        front=(front+1)%size
    
def display():
    if front==-1 and rear==-1:
        print("\nQueue is empty!",end=" ")
        return
    else:
        print("\nVehicle in Toll Plaza : ",end=" ")
        i=front

        while True:
            print(queue[i],end=", ")

            if(i==rear):break
            i=(i+1)%size

#Dry run...
enqueue("Car 1")
enqueue("Car 2")
enqueue("Car 3")
enqueue("Car 4")

display()
dequeue()
display()

enqueue("Car 5")
enqueue("Car 6")
enqueue("Car 7")

display()