#include<iostream>
using namespace std;

int sumOfArr(int arr[],int n){
    int sum=0;
    for(int i=0; i<n; i++){
        sum=sum+arr[i];
    }
    return sum;
}

bool isPossible(int arr[],int n,int m,int mid){
    int pagesum=0;
    int student=1;

    for(int i=0; i<n; i++){
        if(pagesum+arr[i]<=mid){
            pagesum=pagesum+arr[i];
        }
        else{
            student++;
            if (student>m || arr[i]>mid){
                return false;
            }
            pagesum=arr[i];
        }
    }
    return true;
}


int solve(int arr[],int n,int m){
    int start=0;
    int end=sumOfArr(arr,n);
    int mid=start+(end-start)/2;
    int ans=-1;
    while(start<=end){
        if(isPossible(arr,n,m,mid)){
            ans=mid;
            end=mid-1;
        }
        else{
            start=mid+1;
        }
        mid=start+(end-start)/2;
    }
    return ans;
}

int main()
{
    int n=4;
    int memebers=2;
    int arr[4]={10,20,30,40};
    solve(arr,n,memebers);
    
    return 0;
}
