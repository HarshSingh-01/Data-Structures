# Quick Sort

"""
Algorithm:

Function Partition(arr, start, end){
    pivot <- arr[end]
    pIndex <- start-1
    for i <- start to end - 1 {
        if arr[i]<=pivot {
            Swap(arr[i], arr[pIndex])
            pIndex <- pIndex + 1
        }
    } Swap (arr[pIndex+1], arr[end])
} return pIndex+1

Function QuickSort(arr, start=0, end=len(arr)){
    if start<end{
        pIndex <- Partition(arr, start, end)
        QuickSort(arr, start, pIndex-1)
        QuickSort(arr, pIndex+1, end)
    }
}
"""

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start-1

    for i in range(start,end):
        if arr[i]<=pivot:
            pIndex = pIndex + 1
            arr[i], arr[pIndex] = arr[pIndex], arr[i]

    arr[pIndex+1], arr[end] = arr[end], arr[pIndex+1]

    return pIndex+1

def quickSort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        quickSort(arr, start, pIndex-1)
        quickSort(arr, pIndex+1, end)
            

# Testing
array = [9,2,3,5,8,6,7,4,1]

quickSort(array, 0, len(array)-1)

print(array)