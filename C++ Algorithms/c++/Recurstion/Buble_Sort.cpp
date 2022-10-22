#include<iostream>
using namespace std;
void printArr(int arr[], int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void BubleSort(int arr[],int s,int n){
    if(s>n){
        return ;
    }
    if(n==1 || n==0){
        return ;
    }
    for(int i=0; i<n; i++){
    if(arr[i]>arr[i+1]){
        swap(arr[i],arr[i+1]);
    }
}
    s++;
    BubleSort(arr,s,n);
}
int main()
{
    int arr[]={3,5,1,2,4};
    int n=5;
    printArr(arr,n); 
    BubleSort(arr,0,n);
    printArr(arr,n);
    return 0;
}
 