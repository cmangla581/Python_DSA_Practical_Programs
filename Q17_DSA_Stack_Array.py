# Implementation of stack using array 

MAX = 100 
stack = [] 
top = -1 

# Push operation 
def push(x): 
    global top 
    if top == MAX - 1: 
        print("Stack Overflow")
        return  
    stack.append(x) 
    top += 1 
    print(f"{x} pushed to stack") 


def pop():
    global top
    if top == -1:
        print("Stack Underflow")
        return
    print(f"{stack.pop()} popped from stack")
    top -= 1

# Peek operation
def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print(f"Top element is {stack[top]}")

# Display stack
def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(top, -1, -1):
            print(stack[i])

# Example usage
push(10)
push(20)
push(30)

display()

peek()

pop()
pop()

display()