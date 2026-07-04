# Definition

# Backtracking is a problem-solving technique in which we return to a previous state when needed. 
# It is commonly implemented using a Stack, which follows the LIFO (Last In, First Out) principle.

# In this Problem

# The GPS stores the places visited by the user.

# visit(place) → Move to a new place.
# back() → Return to the previously visited place.
# forward() → Move forward again if available.

# This works like the Back and Forward buttons of a web browser. Therefore, two stacks are used:

# Back Stack → Stores previously visited places.
# Forward Stack → Stores places that can be revisited.

backword=[]
forword=[]
current=None

def visit(place):
    global current
    backword.append(current)
    current=place
    forword=[]
    print("Current is : ",current)
    
def back():
    global current
    forword.append(current)
    current=backword.pop()
    print("After Backword Current is : ",current)

def forw():
    global current
    backword.append(current)
    current=forword.pop()
    print("After Forword Current is : ",current)


#Dry run
visit("Palitana")
visit("Bhavnagar")
visit("Ahmedabad")
visit("Garden")

back()
back()
forw()