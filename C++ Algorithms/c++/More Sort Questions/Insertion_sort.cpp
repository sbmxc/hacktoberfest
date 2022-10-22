#include<iostream>
using namespace std;

// In Insertion Sort shifting of elements happen not swapping (Both are diffrent terms)



void printArr(int arr[],int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    int n=5;
    int arr[]={4,2,5,3,1};

    printArr(arr,n);

    for(int i=1; i<n; i++){
        int temp=arr[i];


        int j=i-1;  
        for(;j>=0; j--){

            if (arr[j]>temp){
                arr[j+1]=arr[j];
            }
            else{
                break;
            }

        }
        arr[j+1]=temp;
    }
    
    printArr(arr,n);
    return 0;
}
