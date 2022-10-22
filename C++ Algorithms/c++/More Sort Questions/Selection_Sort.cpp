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
    int n=5;
    int arr[5]={64,25,25,72,11};   
    printArr(arr,n);
    for(int i=0; i<n; i++){
        int min=i;    
        for(int j=i+1; j<n; j++){
            if(arr[j]<arr[min]){
                min=j;
            }
        }
        swap(arr[i],arr[min]);
    }
    printArr(arr,n);
    return 0;
}
