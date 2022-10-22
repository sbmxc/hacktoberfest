#include<iostream>
using namespace std;

bool LinearSearch(int arr[],int n,int key){
   
    if (n==0){return false;}
    
    if(arr[0]==key){
        return true;
    }
    return LinearSearch(arr+1,n-1,key);
}


int main()
{

    int arr[5]={23,34,345,123,45};
    int n=4;
    int key=30;

    cout<<LinearSearch(arr,n,key)<<endl;

    
    return 0;
}
