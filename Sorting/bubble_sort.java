public class BubbleSortExample {  
    static void bubbleSort(int[] arr) {  
        int s = arr.length;  
        int temp = 0;  
         for(int i=0; i < s; i++){  
                 for(int j=1; j < (s-i); j++){  
                          if(arr[j-1] > arr[j])
                          {  
                                 temp = arr[j-1];  
                                 arr[j-1] = arr[j];  
                                 arr[j] = temp;  
                         }  
                          
                 }  
         }  
  
    }  
    public static void main(String[] args) {  
                int arr[] ={22,33,2,4,87,9};  
                 
                System.out.println("Array Before Bubble Sort :- ");  
                for(int i=0; i < arr.length; i++){  
                        System.out.print(arr[i] + " ");  
                }  
                System.out.println();  
                  
                bubbleSort(arr);//sorting array elements using bubble sort  
                 
                System.out.println("Array After Bubble Sort :- ");  
                for(int i=0; i < arr.length; i++){  
                        System.out.print(arr[i] + " ");  
                }  
   
        }  
}  
