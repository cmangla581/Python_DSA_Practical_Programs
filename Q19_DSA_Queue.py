
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return
        
        removed = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        print("Dequeued element:", removed)

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    # Display queue
    def display(self):
        temp = self.front
        
        if temp is None:
            print("Queue is empty")
            return
        
        print("Queue elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.peek()

q.dequeue()
q.display()