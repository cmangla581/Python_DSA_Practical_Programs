r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = []
print("Enter sorted matrix:")

for _ in range(r):
    matrix.append(list(map(int, input().split())))

key = int(input("Enter element to search: "))

low = 0
high = r * c - 1
found = False

while low <= high:
    mid = (low + high) // 2

    row = mid // c
    col = mid % c

    if matrix[row][col] == key:
        print(f"Element found at position ({row}, {col})")
        found = True
        break
    elif matrix[row][col] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")