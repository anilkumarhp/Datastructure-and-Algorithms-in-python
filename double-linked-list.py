class DoubleLinkedList:
    """ Demonstrating double linked list """

    class Node:
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, _next, prev):
            self._element = element
            self._next = _next
            self._prev = prev

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_first(self, e):
        newest = self.Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            newest._prev = None
            self._head._prev = newest
            self._head = newest
        self._size += 1

    def insert_last(self, e):
        newest = self.Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            thead = self._head
            i = 0
            while i < len(self) - 1:
                thead = thead._next
                i += 1
            newest._next = None
            newest._prev = thead
            thead._next = newest
            self._tail = newest
        self._size += 1

    def insert_any_pos(self, e, pos):
        newest = self.Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            self._size += 1
        elif pos == 1:
            self.insert_first(e)
        elif pos > len(self):
            print("position exceeds length hence inserting at end")
            self.insert_last(e)
        else:
            thead = self._head
            i = 0
            while i < pos - 1:
                thead = thead._next
                i += 1
            newest._prev = thead
            newest._next = thead._next
            thead._next = newest
            self._size += 1

    def delete_first(self):
        if self.is_empty():
            print("DLL is empty")
        else:
            print(self._head._element)
            thead = self._head._next
            thead._prev = None
            self._head = thead
            self._size -= 1

    def delete_last(self):
        if self.is_empty():
            print("DLL is empty")
        else:
            print(f'Element removed : {self._tail._element}')
            thead = self._tail._prev
            thead._next = None
            self._tail = thead
            self._size -= 1

    def delete_at_any(self, pos):
        if self.is_empty():
            print("DLL is empty")
        elif pos == 1:
            self.delete_first()
        elif pos >= len(self):
            self.delete_last()
        else:
            thead = self._head
            i = 0
            while i < pos - 1:
                thead = thead._next
                i += 1
            print(f'Element removed : {thead._element}')
            next = thead._next
            thead._prev._next = next
            thead._next._prev = thead._prev
            self._size -= 1

    def display(self):
        thead = self._head
        if self.is_empty():
            print("Empty linked list")
        else:
            size = self._size
            while size:
                print(f'--> {thead._element}', end=" ")
                # print("\n" + str(thead))
                # print(thead._prev)
                # print(thead._next)
                # print()
                thead = thead._next
                size -= 1
        print("\n\n")


# Call the Double linked List
dbl = DoubleLinkedList()

while True:
    if dbl.is_empty():
        print("Enter the first element")
        el = int(input())
        dbl.insert_first(el)
    else:
        print(f"options:\n1 -> add element at start\n2 -> add element at end\n3 -> add element at any position\n4 -> delete at the start\n5 -> delete at the end\n6 -> delete at any position\n7 -> display the element\ne ->  to exit")
        ch = input()
        if ch == 'e' or ch == 'E':
            exit()
        else:
            try:
                ch = int(ch)
            except ValueError:
                print(f"Invalid choice {ch}, try again!!")
                continue
            if ch == 1:
                el = int(input("Enter Element : "))
                dbl.insert_first(el)
            elif ch == 2:
                el = int(input("Enter Element : "))
                dbl.insert_last(el)
            elif ch == 3:
                p = int(input("Enter position : "))
                el = int(input("Enter Element : "))
                dbl.insert_any_pos(el, p)
            elif ch == 4:
                dbl.delete_first()
            elif ch == 5:
                dbl.delete_last()
            elif ch == 6:
                p = int(input("Enter position : "))
                dbl.delete_at_any(p)
            elif ch == 7:
                dbl.display()
            else:
                print(f"Invalid choice {ch}, try again!!")
