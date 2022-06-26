# Insertion Sort

"""
Algorithm:
1. Assume that the first element of the array is already sorted, return 1.
2. Pickup the next element and store that in key. 
3. Now compare all the elements with the key.
4. If the elemented stored in the sorted array is smaller, then move to the next element. Else, 
    shift greater elements in the array to the right.
5. Insert the value
6. Repeat until the array is sorted.

"""

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while (j>=0 and key<=arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr

# Testing
print(insertionSort([21, 1, 43, 5, 10]))
    


