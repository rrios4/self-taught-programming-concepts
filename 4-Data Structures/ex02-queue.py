class Queue:
   def __init__(self):
       self.items = []
 
	 # Checks returns True if the queue is empty and False otherwise
   def is_empty(self):
       return self.items == []
 
	 # Adds a new item to the queue
   def enqueue(self, item):
       self.items.insert(0, item)
 
	 # Removes an item from the queue
   def dequeue(self):
       return self.items.pop()
 
	 # Returns the number of items in the queue
   def size(self):
       return len(self.items)

# Create new queue
a_queue = Queue()

# Add items and check the queue size
for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())

# Remove each item from the queue
for i in range(5):
    print(a_queue.dequeue())

# Print if queue is empty
print(a_queue.is_empty())