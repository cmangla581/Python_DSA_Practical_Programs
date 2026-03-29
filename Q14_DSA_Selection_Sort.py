# Question on the selection sort as: 

def selection_sort(arr): 
    n = len(arr)  

    for i in range(n): 
        min_idx = 1 

        for j in range(i+1, n): 
            if arr[j] < arr[min_idx]: 
                min_idx = j 

        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        return arr 
    

n = int(input("Enter the number of elements: ")) 
arr = list(map(int, input("Enter elements: ").split())) 

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr) 

