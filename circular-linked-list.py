class CircularList:
    """ Demonstrating a circular linked list """

    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, _next):
            self._element = element  # store the element
            self._next = _next  # store the address of next element

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the size of Linked list """
        return self._size

    def is_empty(self):
        """ Checks whether the Linked list is empty and returns True or False"""
        return self._size == 0

    def add_first(self, e):
        """ adds element to the beginning """
        newset = self.Node(e, None)
        if self.is_empty():
            self._head = newset
            self._tail = newset
        else:
            self._tail._next = newset
            newset._next = self._head
            self._head = newset
        self._size += 1

    def add_last(self, e):
        """ adds element to the end """
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def add_at_any(self, e, pos):
        """ add element at any given position """
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            thead = self._head
            i = 1
            while i < pos-1:
                thead = thead._next
                i += 1
            newest._next = thead._next
            thead._next = newest
        self._size += 1

    def remove_first(self):
        """ Removes element at the start """
        if self.is_empty():
            print("Linked list is empty")
        else:
            thead = self._head
            self._head = thead._next
            self._tail = thead._next
            print(thead._element)
            self._size -= 1

    def remove_last(self):
        """ Removes element at the end """
        if self.is_empty():
            print("Linked list is empty")
        else:
            thead = self._head
            i = 0
            while i < len(self) - 2:
                thead = thead._next
                i += 1
            self._tail = thead
            thead = thead._next
            thead = thead._element
            self._tail._next = self._head
            print(thead)
            self._size -= 1

    def remove_at_any(self, pos):
        """ Removes element from a given position """
        if self.is_empty():
            print("Linked list is empty")
        elif pos == 1:
            thead = self._head
            print(thead._element)
            self._head = thead._next
        else:
            thead = self._head
            i = 1
            while i < pos - 1:
                thead = thead._next
                i += 1
            value = thead._next._element
            thead._next = thead._next._next
            print(value)
        self._size -= 1

    def display(self):
        thead = self._head
        if self.is_empty():
            print("Empty linked list")
        else:
            size = self._size
            while size:
                print(thead._element, end='-->')
                thead = thead._next
                size -= 1
        print()


cll = CircularList()

cll.add_first(10)
cll.add_first(20)
cll.display()
# cll.add_first(30)
# cll.display()
# cll.add_last(40)
# cll.display()
# cll.add_last(50)
# cll.display()
# cll.add_at_any(60, 2)
# cll.display()
# cll.add_first(80)
# cll.display()
# cll.add_last(90)
# cll.display()
# cll.add_at_any(70, 4)
# print(cll.__len__())
# cll.display()
#
cll.remove_first()
print(cll.__len__())
cll.display()

cll.remove_last()
cll.display()
# print(cll.__len__())
# cll.remove_last()
# cll.display()
# print(cll.__len__())
#
# print("remove at last")
# cll.remove_at_any(3)
# print(cll.__len__())
# cll.display()
#
#
# cll.remove_at_any(1)
# print(cll.__len__())
# cll.display()
#
