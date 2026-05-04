
# Write a Python Program to traverse Binary tree using the array 

def preorder(tree, i) : 
    if i >= len(tree) or tree[i] is None: 
        return 
    
    print(tree[i], end = " ") 
    preorder(tree, 2*i + 1)  
    preorder(tree, 2*i + 2)  


n = int(input("Enter the number of nodes: ")) 
tree = [] 

print("Enter elements (use None for NULL):")
for _ in range(n):
    val = input()
    tree.append(None if val == "None" else int(val))

print("Preorder Traversal:")
preorder(tree, 0) 