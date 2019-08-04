from random import randint


class Queue:
    """
        Queue operations: using list and list methods:
        (First In First Out)
        1) enqueue() : add value to list
        2) dequeue() : remove value from the front.
        3) is_empty() : check whether queue is empty
        4) qsize() : returns queue size
    """

    def __init__(self):
        """ initialize the queue  and its size """
        self.queue = []
        self.size = 0

    def enqueue(self, val):
        """ add element to the queue """
        self.queue.append(val)

    def dequeue(self):
        """ Remove element from the queue """
        if self.queue:
            p = self.queue.pop(0)
            print(p)
        else:
            print("Queue is empty")

    def is_empty(self):
        """ Checks whether queue is empty. """
        if not self.queue:
            print("Queue is empty")

    def qsize(self):
        """ Returns queue size """
        self.size = len(self.queue)
        return self.size

    def display(self):
        """ Display queue size """
        if self.queue:
            print(self.queue)
        else:
            print("Queue is empty")


q = Queue()

for i in range(10, 100, randint(10, 20)):
    q.enqueue(i)
q.display()
print(f'Size : {q.qsize()}')

for i in range(q.qsize() + 1):
    q.dequeue()
