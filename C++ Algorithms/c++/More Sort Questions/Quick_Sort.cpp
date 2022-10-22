#include<iostream>
using namespace std;


int Partition(int arr[],int s,int e){
    int pivot=arr[s];

    //Count all element that is less than pivot
    int counter=0;
    for(int w=s+1; w<=e; w++ ){
        if(arr[w]<=pivot){
            counter++;
        }
    }
    //place the pivot element in correct place
    int pivotIndex=s+counter;
    swap(arr[pivotIndex],arr[s]);

    //Setting right and left index to sort both side by swaping
    int i=s;
    int j=e;
    
    //till i chota h jaha pivot element h or j bada h jaha pivot element h
    while(i<pivotIndex && j>pivotIndex){

        //pivot ++ kar do jaha tak arr ka element chota h pivot se
        while(pivot>=arr[i]){
            i++;
        }
        //pivot ++ kar do jaha tak arr ka element bada h pivot se
        while(pivot<arr[j]){
            j--;
        }
        
        //swap kar do agar element ho rahe h to
        if(i<pivotIndex && j>pivotIndex){
            swap(arr[i++],arr[j--]);
        }
    }
    return pivotIndex;

}


void quickSort(int arr[], int s ,int e){
    if(s>=e){
        return ;
    }

    //Finding right index for pivot element
    int p=Partition(arr,s,e);

    //Left side sort
    quickSort(arr,s,p-1);
    //Right side sort
    quickSort(arr,p+1,e);
}

int main()
{
    int n=10;
    int arr[10]={40,34,12,4,67,31,53,65,32,75};
    quickSort(arr,0,n-1);

    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
