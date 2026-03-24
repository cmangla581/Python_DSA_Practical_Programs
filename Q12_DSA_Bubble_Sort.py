# Performing the bubble sort with the python code as: 

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Taking input
arr = list(map(int, input("Enter elements separated by space: ").split()))

bubble_sort(arr)

print("Sorted array:", arr)