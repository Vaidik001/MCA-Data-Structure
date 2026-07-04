#A Stack is a linear data structure that follows the 
# LIFO (Last In, First Out) principle. The last element 
# added to the stack is the first one to be removed. 
# It is commonly used in Undo/Redo operations, browser history, 
# and function calls.

class TextEditor:
    def __init__(self):
        self.stack = []

    def type(self, ch):
        self.stack.append(ch)

    def undo(self):
        if self.stack:
            self.stack.pop()

    def getText(self):
        return "".join(self.stack)


e = TextEditor()

#Dry run
e.type("H")
e.type("E")
e.type("L")
e.type("L")
e.type("O")

print("Text :", e.getText())
e.undo()
print("After Undo :", e.getText())