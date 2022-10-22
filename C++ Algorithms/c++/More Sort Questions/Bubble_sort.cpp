#include<iostream>
using namespace std;

void printArr(int arr[],int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void swap(int* a,int* b){
    int temp=*a;
    *a=*b;
    *b=temp;
}



int main()
{
    int n=6;
    int arr[6]={5,6,4,2,1,3};

    printArr(arr,n);
    for(int i=0; i<n; i++){

        for(int j=0; j<n-i-1; j++){
            if (arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
            }
        }
    }
    printArr(arr,n);

    return 0;
}
