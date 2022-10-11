def SelectionSort(A,n):
    for i in range(0,n):
        i_min = i   #we are assuming first index's value to be minimum, further will compare it with other indexes  
        for j in range(i+1, n):
            if A[j] < A[i_min]:
                i_min = j

        temp = A[i_min]  # temp variable to swap the elements
        A[i_min] = A[i]
        A[i] = temp
        print(A)        #to print the sequence in every pass just to get more clarity, its optional
    print("This array is sorted through Selection Sort Algorithm!")
    print(A)            #to print the final sorted array
A = [7,2,4,1,5,3]
n = len(A)
SelectionSort(A,n)  
  