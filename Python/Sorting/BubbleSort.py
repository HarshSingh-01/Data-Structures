# Bubble Sort
"""

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

"""
Optimized buble sort algortithm
bubbleSort(arr)
    swapped <- false
    for i <- 1 to indexOfLastUnsortedElement - 1
        if leftElement > rightElement
            swap leftElement and rightElement
            swapped <- true
end bubbleSort
"""

def optimizedBubbleSort(arr):
    swapped = False
    for step in range(len(arr)):
        for i in range(0, len(arr) - step - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr
                

# Testing
array = [21, -1, 43, -5, 10]
print("Ascending Order: ", optimizedBubbleSort(array))
# print("Descendign Order:", bubbleSortDesc(array))
