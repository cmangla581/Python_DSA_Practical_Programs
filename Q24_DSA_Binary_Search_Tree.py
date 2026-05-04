
# Implementation of the Binary Search Tree using the Array  

SIZE = 100 
tree = [-1] * SIZE 

def insert(value, index): 
    if index >= SIZE: 
        print("Tree Overflow") 
        return 
    
    if tree[index] == -1: 
        tree[index] = value 
        return  

    if value < tree[index]: 
        insert(value, 2*index + 1)
    else: 
        insert(value, 2*index + 2) 


def inorder(index):
    if index >= SIZE or tree[index] == -1:
        return

    inorder(2 * index + 1)
    print(tree[index], end=" ")
    inorder(2 * index + 2)

# Main
insert(50, 0)
insert(30, 0)
insert(70, 0)
insert(20, 0)
insert(40, 0)
insert(60, 0)
insert(80, 0)

print("Inorder Traversal:", end=" ")
inorder(0)
