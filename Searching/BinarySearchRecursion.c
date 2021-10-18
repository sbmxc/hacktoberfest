#include<stdio.h>

int BinarySearch(int arr[],int beg,int end,int key){
	int mid = (beg+end)/2;
	if(beg>end)
		return -1;
	if(arr[mid]==key)
		return mid;
	else if(arr[mid]>key)
		return BinarySearch(arr,beg,mid-1,key);
	else
		return BinarySearch(arr,mid+1,end,key);
}
int main(){
	int n,key,arr[20],index,i;
	
	printf("Enter number of elements in the array: ");
	scanf("%d",&n);
	printf("\nEnter array elements: ");
	for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	printf("\nEnter element to search: ");
	scanf("%d",&key);
	
	index = BinarySearch(arr,0,n-1,key);
	
	if(index==-1)
		printf("Given element not found in the array");
	else
		printf("Element found at position: %d",index+1);
		
	return 0;
}
