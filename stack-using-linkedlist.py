class Stack:
    class Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, _next):
            self._element = element
            self._next = _next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self.Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print(self._head._element)
            self._head = self._head._next
            self._size -= 1

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end='-->')
            temp = temp._next
        print()


s = Stack()
s.push(13)
s.push(24)
s.push(10)
s.push(35)
s.push(30)
s.push(40)
s.display()
s.pop()
s.pop()
s.pop()
s.display()
