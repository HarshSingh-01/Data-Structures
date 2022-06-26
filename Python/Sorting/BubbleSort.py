# Bubble Sort

"""
Example 

Here we sort the following sequence using bubble sort

Sequence: 2, 23, 10, 1

First Iteration

(2, 23, 10, 1) –> (2, 23, 10, 1), Here the first 2 elements are compared and remain the same because they are already in ascending order.

(2, 23, 10, 1) –> (2, 10, 23, 1), Here 2nd and 3rd elements are compared and swapped(10 is less than 23) according to ascending order.

(2, 10, 23, 1) –> (2, 10, 1, 23), Here 3rd and 4th elements are compared and swapped(1 is less than 23) according to ascending order

At the end of the first iteration, the largest element is at the rightmost position which is sorted correctly.

Second Iteration

(2, 10, 1, 23) –> (2, 10, 1, 23), Here again, the first 2 elements are compared and remain the same because they are already in ascending order.

(2, 10, 1, 23) –> (2, 1, 10, 23), Here 2nd and 3rd elements are compared and swapped(1 is less than 10) in ascending order.

At the end of the second iteration, the second largest element is at the adjacent position to the largest element.

Third Iteration

(2, 1, 10, 23) –> (1, 2, 10, 23), Here the first 2 elements are compared and swap according to ascending order.

The remaining elements are already sorted in the first and second Iterations. After the three iterations, the given array is sorted in ascending order. So the final result is 1, 2, 10, 23.


Logic:

Ascending Order: if arr[j] > arr[j+1]: arr[j], arr[j+1] =  arr[j+1], arr[j]
Descending Order: if arr[j+1]> arr[j]: arr[j+1], arr[j] = arr[j], arr[j+1]

Algorithm:
begin bubbleSort(arr)
    for all the elements in arr
        if arr[i]>arr[i+1]
            swap(arr[i], arr[i+1])
        end if
    end for
    return arr
end bubbleSort
"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# def bubbleSortDesc(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j+1]>arr[j]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     return arr

# Testing
array = [21, 1, 43, 5, 10]
print("Ascending Order: ", bubbleSort(array))
# print("Descendign Order:", bubbleSortDesc(array))
