from random import randint


class Dequeue:
    """
        Dequeue operations: using list and list methods

        1) add_first() : add element at the first position
        2) add_last() : add element at the last position
        3) delete_first() :  delete element from 1st position
        4) delete_last() : delete element at the last position
        5) display() : prints the element in the dequeue
    """

    def __init__(self):
        """ Initializing the dequeue """
        self.dequeue = []

    def add_first(self, val):
        """ Add element at the first position """
        self.dequeue.insert(0, val)

    def add_last(self, val):
        """ add element at the last position """
        self.dequeue.append(val)

    def delete_first(self):
        try:
            p = self.dequeue.pop(0)
            print(p)
        except IndexError:
            print("dequeue is empty")

    def delete_last(self):
        try:
            p = self.dequeue.pop()
            print(p)
        except IndexError:
            print("dequeue is empty")

    def display(self):
        print(self.dequeue)

    def dqsize(self):
        return len(self.dequeue)


q = Dequeue()

for i in range(10, 100, randint(10, 15)):
    if i % 2 == 0:
        q.add_first(i)
        q.display()
    else:
        q.add_last(i)
        q.display()


print(f'Size : {q.dqsize()}')

for i in range(q.dqsize() + 1):
    if not i % 2 == 0:
        q.delete_first()
    else:
        q.delete_last()
