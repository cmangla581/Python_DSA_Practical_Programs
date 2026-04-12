
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class
class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        
        popped = self.top.data
        self.top = self.top.next
        print("Popped element:", popped)

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display stack
    def display(self):
        temp = self.top
        
        if temp is None:
            print("Stack is empty")
            return
        
        print("Stack elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

s.peek()

s.pop()
s.display()