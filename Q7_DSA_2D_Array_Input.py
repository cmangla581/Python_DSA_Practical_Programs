
# Input of the array 

rows = int(input("Enter the rows: ")) 
cols = int(input("Enter the columns: ")) 

matrix = [] 

for i in range(rows): 
    row = list(map(int, input().split())) 
    matrix.append(row) 

print("2D Matrix:\n") 

for row in matrix: 
    print(row)  


