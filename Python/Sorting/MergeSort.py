# Merge Sort

"""
Algorithm:
Step 1. Define the mid value, mid  =  int(len(arr)/2)
Step 2. Define the Left and subarray, L =  arr[:mid] and R = arr[mid:]
Step 3. Recall the merge function for Left sub array and Right sub array,  
        mergeSort(L)
        mergeSort(R)
Step 4. Initialise i = j = k = 0, 'i', 'j', 'k' are for indexing Left, Right and Main Array.
Step 5. Check the condition if len(arr)>1
Step 6. Create a while loop with conditon i < len(LeftSubArray) && j M len(RightSubArray)
        a. Check the condition if LeftSubArray[i] < RightSubArray[j], then 
            Arr[k] = LeftSubarray[i]
            Increment i, i = i + 1
        b. Else,
            Arr[k] = RightSubArray[j]
            Increment j, j = j + 1

        Increment k, k = k +1
Step 7. Create a another while loop for inserting the leftover element of LeftSubArray in main array 
        begin while loop (i< len(LeftSubArray))
            Arr[k] = LeftSubArray[i]
            k = k + 1
            i = i + 1
        end while loop
Step 8. Create a another while loop for insertion the leftover element of RightSubArray in main array
        begin while loop (j<len(RightSubArray))
            Arr[k] = LeftSubArray[j]
            k = k + 1
            j = j + 1
        end while loop
"""

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2

        # Left Sub Array
        L = arr[:mid]

        # Right Sub Array
        R = arr[mid:]

        # Sorting the Left Sub Array
        mergeSort(L)

        # Sorting the Right Sub Array
        mergeSort(R)

        # Creating while loop 
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1

        # Checking if any element left in Left sub array
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1
        
        # Checking if any element left in Right sub array
        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1

        
            
# Testing 
array = [9,2,3,5,8,6,7,4,1]

mergeSort(array)

print("Sorted Array:", array)
