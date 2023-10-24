/*
 QUESTION:Given an array of n distinct integers sorted in ascending order,
  write a function that returns a Fixed Point in the array,
  if there is any Fixed Point present in array, else returns -1. 
 Fixed Point in an array is an index i such that arr[i] is equal to i. 
 Note that integers in array can be negative. 
 
 Time Complexity: O(n) 
 Auxiliary Space: O(1) */
 class fixed_point_equal_to_index { 
    static int linearSearch(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; i++) { 
            if (arr[i] == i) 
                return i; 
        } 
        return -1; 
    } 

    public static void main(String args[]) 
    { 
        int arr[] = { -10, -1, 0, 3, 10, 11, 30, 50, 100 }; 
        int n = arr.length; 
        System.out.println("Fixed Point is "
                           + linearSearch(arr, n)); 
    } 
}               