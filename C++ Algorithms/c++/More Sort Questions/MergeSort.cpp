#include<iostream>
using namespace std;




void Merge(int *arr,int s, int e){
    int mid =s+(e-s)/2;

    // length of arr 1 and arr 2 
    int len1=mid-s+1;
    int len2=e-mid;

    // Do new arr banaye ge aur frr dono ko hemerge kar denge
    int *first=new int[len1];
    int *second=new int[len2];

    // copying element in arr
    int MainArrayIndex=s; 
    for(int i=0; i<len1; i++){
        first[i] = arr[MainArrayIndex++];
    }
    
    MainArrayIndex=mid+1;
    for(int j=0; j<len2; j++){
        second[j]= arr[MainArrayIndex++];
    }

    // Merge 2 sorted arr
    int index1=0;
    int index2=0;
    MainArrayIndex=s;
    while(index1<len1 && index2<len2){

        //compare which arr element is small goes first
        if(first[index1]<second[index2]){
            arr[MainArrayIndex++]=first[index1++];
        }
        else{
            arr[MainArrayIndex++]=second[index2++];
        }
    }
// For remaining element
    while(index1<len1){
        arr[MainArrayIndex++]=first[index1++];
    }
    while(index2<len2){
        arr[MainArrayIndex++]=second[index2++];
    }

    //delete memory of arrays from heap
    delete []first;
    delete []second;

}


void MergeSort(int *arr,int s,int e){
    if(s>=e){
        return ;
    }

    int mid=s+(e-s)/2;

    //Left side
    MergeSort(arr,s,mid);

    //Right side
    MergeSort(arr,mid+1,e);


    //Merge kar dege dono arr ko / conqure
    Merge(arr,s,e); 
}


int main()
{
    int n=10;
    int arr[]={5,4,3,6,7,8,9,1,10,0};

    MergeSort(arr,0,n-1);

    for(int i=0; i<n; i++){
        cout<<arr[i]<<" "; 
    }
    cout<<endl;
    

    return 0;
}
