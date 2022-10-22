// Binary Search Using Pivot Element 

// steps are:
// 1) find pivot element
// 2) choose the line by pivot element -> in which we have to apply the binary search   
// 3) By binary search we can find the target

#include <iostream>
using namespace std;
int PivotElement(int arr[], int n){
    int s=0;
    int e=n-1;

    int mid=s+(e-s)/2;
    while(s<e){
        if (arr[mid]>=arr[0]){
            s=mid+1;
        }
        else{
            e=mid;
        }
        mid=s+(e-s)/2;

    }

    return s;

}

int BinarySearch(int arr[],int st,int en,int key){
    
    int s=st;
    int e=en;
    int mid=s+(e-s)/2;

    while(s<=e){

        if(arr[mid]==key){
            return mid;   
        }
        if (arr[mid]<key){
            s=mid+1;
        }
        else {
            e=mid-1;
            
        }
        mid=s+(e-s)/2;

    }
    return -1;   
}

int main()
{
    int key=3;
    int n=5;
    int arr[5]={8,10,1,2,3};
    int pivot=PivotElement(arr,n);
    cout<<"Pivot is at index "<<pivot<<endl;
    int value;
    if (key>=arr[pivot] && key<=arr[n-1]){
         value=BinarySearch(arr,pivot,n-1,key);
    }
    else{
        value=BinarySearch(arr,0,pivot-1,key);
    }
    cout<<"Value is at index "<<value<<endl;

    return 0;
}
