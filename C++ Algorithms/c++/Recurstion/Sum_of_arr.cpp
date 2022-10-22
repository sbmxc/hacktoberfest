
#include<iostream>
using namespace std; 

int sum(int arr[],int n){
    if(n==0){return 0;}
    if (n==1){return arr[0];}

    int rem=sum(arr+1,n-1);
    int sum=arr[0]+rem;
    return sum;

}


int main(int argc, char const *argv[])
{
    int n=7;
    int arr[]={1,2,3,4,5,6,10};
    cout<<sum(arr,n)<<endl;

    return 0;
}
