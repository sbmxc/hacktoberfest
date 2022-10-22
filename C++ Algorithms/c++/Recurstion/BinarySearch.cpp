#include<iostream>
using namespace std;


bool BinarySearch(int arr[],int s,int e,int key){
    if(s>e){return false;}

    int mid=s+(e-s)/2;

    if(arr[mid]==key){
        return true;
    }
    else if(arr[mid]>key){
        e=mid-1;
        return BinarySearch(arr,s,e,key);
    }
    else{
        s=mid+1; 
        return BinarySearch(arr,s,e,key);
    }


}

int main()
{
    int n=6;
    int arr[]={1,2,3,3,5,6,7};
    int key=4;

    cout<<BinarySearch(arr,0,n,key)<<endl;

    
    return 0;
}
