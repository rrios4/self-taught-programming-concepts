import time
import random
 
 
class Queue:
    def __init__(self):
        self.items = []
 
 
    def is_empty(self):
        return self.items == []
 
 
    def enqueue(self, item):
        self.items.insert(0, item)
 
 
    def dequeue(self):
        return self.items.pop()
 
 
    def size(self):
        return len(self.items)
 
    # Simulates selling tickets to a line of people. 
    # till_show represents the number of seconds until the show starts and there is no time to left to buy tickets
    # max_time represents the longest amount of time (in seconds) it takes for a person to buy a ticket.
    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []
 
        for i in range(10):
            pq.enqueue("person " + str(i))

        # Find the result of the time function plus the number of seconds passed in as the variable till_show
        t_end = time.time()\
                + till_show
        now = time.time()
        while now < t_end \
        and not pq.is_empty():
            now = time.time()
            r = random.\
                randint(0,
                        max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)
 
 
        return tix_sold
 
 
queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)