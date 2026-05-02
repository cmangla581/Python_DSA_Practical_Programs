# Convert the infix expression to prefix and the postfix 

def precedence(op): 
    if op == '^': 
        return 3 
    
    elif op in ('*', '/'): 
        return 2 
    
    elif op in ('+', '-'): 
        return 1 
    
    return 0 

def infix_to_postfix(infix): 
    stack = [] 
    postfix = [] 

    for ch in infix: 
        if ch.isalnum(): 
            postfix.append(ch) 

        elif ch == '(': 
            stack.append(ch) 

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  

        else: 
            while (stack and precedence(stack[-1]) >= precedence(ch)):
                postfix.append(stack.pop())
            stack.append(ch) 

    while stack: 
        postfix.append(stack.pop()) 

    return ''.join(postfix) 


def infix_to_prefix(infix):
    # Reverse infix
    infix = infix[::-1]

    # Swap brackets
    new_infix = ""
    for ch in infix:
        if ch == '(':
            new_infix += ')'
        elif ch == ')':
            new_infix += '('
        else:
            new_infix += ch

    # Convert to postfix
    postfix = infix_to_postfix(new_infix)

    # Reverse postfix to get prefix
    prefix = postfix[::-1]
    return prefix 

infix = input("Enter the infix expression: ") 

postfix = infix_to_postfix(infix)
prefix = infix_to_prefix(infix)

print("Postfix:", postfix)
print("Prefix :", prefix)


    
