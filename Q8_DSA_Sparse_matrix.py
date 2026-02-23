
r = int(input("Enter the number of rows:"))
c= int(input("Enter the number of columns:")) 

matrix = [] 
zero_count = 0 
non_zero_count = 0 
total_sum = 0 

print("Enter the matrix elements:") 

for i in range(r): 
    row = list(map(int, input().split())) 
    matrix.append(row) 

elements = [num for row in matrix for num in row] 

# count zeros and compute sum 

for num in elements: 
    total_sum += num 

    if num ==0: 
        zero_count == 1 
    
    else: 
        non_zero_count += 1 

if zero_count > non_zero_count: 
    print("\n matrix is sparse\n") 
else: 
    print("matrix is not sparse") 

unique_elements = list(set(elements)) 
unique_elements.sort() 

minimum = unique_elements[0] 
maximum =  unique_elements[-1] 

if len(unique_elements) > 1: 
    second_min = unique_elements[1]
    second_max = unique_elements[-2] 

else: 
    second_min = "not avaailable" 
    secon_max = "Not available" 

print("Sum of elements =", total_sum)
print("Maximum element =", maximum)
print("Second Maximum element =", second_max)
print("Minimum element =", minimum)
print("Second Minimum element =", second_min)
