# The sum of the array elements with the input as: 

rows = int(input("Enter the number of rows: ")) 
cols = int(input("Enter the number of columns: ")) 

arr = [] 

print("Enter the elements: ") 

for i in range(rows): 
    row = [] 
    for j in range(cols): 
        val = int(input(f"Element [{i}][{j}]: ")) 
        row.append(val) 
    arr.append(row) 

# Calculating the sum  
total_sum = 0 
for i in range(rows): 
    for j in range(cols): 
        total_sum += arr[i][j] 

print("The 2D array is: ") 
for r in arr: 
    print(r) 

print("Sum of all elements: ", total_sum) 
