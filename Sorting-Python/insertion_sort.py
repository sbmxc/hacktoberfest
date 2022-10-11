def InsertionSort(A,n):
    for i in range(0,n-1):   # this outer loop will run till n-2(where n is length of array)
        for j in range(i+1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j] # swapping the elements
        print(A) #to print the sequence in every pass just to get more clarity,it's optional
    print("This array is sorted through Insertion Sort Algorithm!")
    print(A)

A = [7,2,4,1,5,3]
n = len(A)
InsertionSort(A,n)

