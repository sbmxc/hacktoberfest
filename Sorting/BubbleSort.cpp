#include <iostream>
using namespace std;

//Bubble Sort Recursively
//Time Complexity O(N^2) if Array not Sorted
//Time Complexity O(N) if Array is Sorted 

void bubbleSort(int array[], int n)
{
    if (n == 0 || n == 1)
    {
        return;
    }
    for (int i = 0; i < n - 1; i++)
    {
        if (array[i] > array[i + 1])
        {
            //swaping array elements if previous element is greater than next element
            swap(array[i], array[i + 1]);
        }
    }
    bubbleSort(array, n - 1);
}

int main()
{
    //Asking the size of array from user
    cout<<"Enter size of Array \n";
    int n;
    cin>>n;

    int array[n];

    // Taking elements of array from user
    cout<<"\nEnter the elements of Array \n";
    for(int i=0;i<n;i++)
    {
        cin>>array[i];
    }
    
    
    //Applying Bubble Sort
    bubbleSort(array, n);
    
    // Printing Array elements after applying Bubble Sort
    cout<<"\nPrinting Array elements after applying Bubble Sort \n";
    for (int i = 0; i < n; i++)
    {
        cout << array[i] << " ";
    }
    return 0;
}