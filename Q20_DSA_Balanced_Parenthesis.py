# Write a code for balanced parenthesis 

def is_balanced(expr): 
    stack = [] 
    pairs = {')': '(', '}': '{', ']': '['} 

    for char in expr: 
        if char in "({[": 
            stack.append(char) 
            
        elif char in "]})": 
            if not stack or stack[-1] != pairs[char]: 
                return False 
            
            stack.pop() 

    return len(stack) == 0 

expr = input("Enter expression: ")

if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")  
             
        
