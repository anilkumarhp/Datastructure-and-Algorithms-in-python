class Stack:
    """
        Implementing the stack operation
        1) push
        2) pop
        3) display
    """
    def __init__(self):
        """ Initialize the stack """
        self.stack = []

    def push(self, val):
        """ Insert value to the top of the stack """
        self.stack.append(val)

    def pop(self):
        """ Remove value from the top of the stack """
        try:
            p = self.stack.pop()
            print(p)
        except IndexError:
            print("Stack is Empty!")

    def is_empty(self):
        if self.stack:
            print("Stack is not empty")
        else:
            print("Stack is empty")

    def display(self):
        """ Display the values in the stack """
        if self.stack:
            print(self.stack)
        else:
            print("Stack is empty")


st = Stack()
for i in range(10, 100, 10):
    st.push(i)

st.display()
st.is_empty()

for i in range(len(st.stack) + 1):
    st.pop()

st.display()
