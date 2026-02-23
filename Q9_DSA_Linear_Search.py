
n = int(input("Enter the size of array:")) 

arr = list(map(int, input("Enter theelements: ").split())) 

key = int(input("Enter elements to search; ")) 

found  =False 

for i in range(n): 
    if arr[i] ==key: 
        print("Element found at position", i+1)
        found = True 
        break 

if not found: 
    print("Element not found")  
