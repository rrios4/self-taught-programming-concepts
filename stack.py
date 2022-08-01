# Creates a empty stack that allows many functions to add, remove, read, and get size
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self): 
        return len(self.items)

stack = Stack()
# pushes 1 as an item to the stack
stack.push(1)
print(stack.is_empty())