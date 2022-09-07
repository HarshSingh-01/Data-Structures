# Selection Sort 

"""
Alogrithm
1. Loop, step = range from 0 to size-1
2. define min_index = i
3. Nested loop under size, i = range from step+1 to size-1 (Second loop is for comparing arr[min_index] element from arr[1,2.....size-1])
4. if arr[min_index]>arr[i], then change the min_index = i
5. Swap the values of arr[step] and arr[min_index] (after doing that you will get smallest number at the min_index.
"""

def selectionSort(array, size):

   for step in range(size):
        min_idx = step

        for i in range(step+1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

   return array
# Testing
array = [7, 2, 1, 6]
size = len(array)

print("Sorted Array:",selectionSort(array, size))