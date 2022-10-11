def BubbleSort(A,n):
    for i in range(1,n):  # here n is len(A), it will run till n-1 
        for j in range(0, n-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]  #swapping the elements which satisfy the if statement
        print(A)  #to print the sequence in every pass just to get more clarity,its optional
    print("This array is sorted through Bubble Sort Algorithm!")
    print(A)      #to print the final sorted array

A = [7,2,4,1,5,3]
n = len(A)
BubbleSort(A,n)
