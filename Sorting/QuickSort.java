import java.util.Scanner;

public class QUICKSORT {

/* Time Complexity : 
   
    Best Case :	O(n*logn)
    Average Case: O(n*logn)
    Worst Case: O(n^2)
    
*/
	public static void main(String[] args) {
		System.out.println("Quick Sort : ");
		
		System.out.print("Enter the size of array : ");
		try (Scanner sc = new Scanner(System.in)) {
			int n = sc.nextInt();
			int a[] = new int[n];

			System.out.println("Enter elements : ");
			for (int i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}

			System.out.println("Array before sorting : ");
			for (int i : a) {
				System.out.print(i + " ");
			}

			
			quickSort(a, 0, a.length - 1); // calling the function

			
			System.out.println("\nArray after sorting : ");
			for (int i : a) {
				System.out.print(i + " ");
			}
		}
	}

	private static void quickSort(int[] a, int low, int high) {
		if (low >= high) {
			return;
		}
		
		int pivotIndex = partition(a, low, high); // pivot index

		
		quickSort(a, low, pivotIndex - 1);
		quickSort(a, pivotIndex + 1, high);
	}

	private static int partition(int[] a, int low, int high) {
		int pivot = a[high];

		int i = low - 1; // just imagine it like it is creating blank places in array

		for (int j = low; j < high; j++) {
			if (a[j] < pivot) {
				i++;
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}

//		now put pivot at correct position i.e., ith

		i++;

		int temp = a[i];
		a[i] = a[high];
		a[high] = temp;
		return i;
	}
}