// package Sorting_Algo;

/****************************   Bubble Sort 

       ->  Algorithm

    bubbleSort(array, sizeOfArray)
    for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
    end bubbleSort


       -> Time Complexity 
          Best	    O(n)
          Worst	    O(n2)
          Average	O(n2)

       -> Space Complexity	O(1)
*/

import java.util.Arrays;

public class BubbleSort {

    public static int[] bubbleSort(int[] arr, int n) {
        
        // loop to access each array element
        for (int i = 0; i < n - 1; i++) {

            // loop to compare adjacent elements
            for (int j = 0; j < n - i - 1; j++) {
            
                // compare two array elements
                if (arr[j] > arr[j + 1]) {
            
                    // swap arr[j+1] and arr[j]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr; // return sorted array
    }
    public static void main(String[] args) {

        int[] arr = {34, 10, 43, 2, 6, 11, 8};
        int n = arr.length;

        System.out.println("The Array in Ascending order:");
        System.out.println(Arrays.toString(bubbleSort(arr, n)));
    }
}
