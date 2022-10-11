'''
Quick Sort properties:
* It uses a strategy of Divide and Conquer Algorithm
* It is an In-place Sorting Algorithm, acquires no additional space but a bit of recursion stack memory space * only
* Uses pivot as the element such that all the elements smaller than pivot should be on the LHS and all the elements greater than the pivot should be on the RHS 
Time- Complexity:
* Best and Average Case -> O(nlog n)
* Worst Case -> O(n^2)

'''

# Taking pivot as any random element of the array
import random

def QuickSort(A, start, end):
    if (start < end):  # checking if the array has atleast 2 elements to proceed further 
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex-1) # applying quicksort on left half of the pivot
        QuickSort(A, pIndex+1, end)   # applying quicksort on right half of the pivot  
        

def Partition(A, start, end): # with this method the pivot will return at its correct position
    pivot = random.choice(A)    # Taking pivot as the last element of the array
    pIndex = start    # pivot index, it will compare with the 'i' values and replace the pivot at the end

    for i in range(start, end+1):
        if (A[i] < pivot):  # condition
            A[i], A[pIndex] = A[pIndex], A[i]  # swaps the elements which satisfy the condition
            pIndex += 1
    
    A[pIndex], pivot = pivot, A[pIndex]   # swaps the pivot with the pivot index
    print(pivot)
    return pIndex                         # returns pivot index(pivot at its correct position)
                          


A = [7,2,1,6,8,5,3,4]
QuickSort(A, 0, len(A)-1)
print(A)        #print final result array


