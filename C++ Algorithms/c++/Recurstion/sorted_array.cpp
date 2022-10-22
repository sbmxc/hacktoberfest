#include<iostream>
using namespace std;



bool isSorted(int arr[], int n){
    
    if(n==0){return true;}
    if(n==1){return true;}

    if(arr[0]>arr[1]){return false;}

    else{bool remainingArr=isSorted(arr+1,n-1);return remainingArr;}

}


int main(int argc, char const *argv[])
{
    int n=6;
    int arr[]={12,43,52,123,5423,54342};
    
    cout<<isSorted(arr,n)<<endl;

    
    return 0;
}
