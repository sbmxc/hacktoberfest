def Merge_sort(A):
    if len(A) > 1: 
        mid = len(A)//2  # Finding the mid-point of the array
        L = A[:mid] # Dividing the array 
        R = A[mid:] # into two halves

        Merge_sort(L) # Sorting the first half
        Merge_sort(R) # Sorting the second half

        i = j = k = 0 

        while i < len(L) and j < len(R): #logic
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
            
A= [2,4,1,6,8,5,3,7]
Merge_sort(A)
print(A)
