# Selection Sort 

"""
Logic:
1. Loop, i = range from 0 to len(arr)-1
2. define min_index = i
3. Nested loop under i, j = range from i+1 to len(arr)-1 (Second loop is for comparing arr[min_index] element from arr[1,2.....size-1])
4. if arr[min_index]>arr[j], then change the min_index = j
5. Swap the values of arr[i] and arr[min_index] (after doing that you will get smallest number at the min_index.

"""

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                # Getting new minimum index
                min_index = j
        # Swaping        
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

# Testing
array = [7, 2, 1, 6]

print("Sorted Array:",selectionSort(array))