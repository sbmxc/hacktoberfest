
int sumOfArr(vector<int> arr,int n){
    int sum=0;
    for(int i=0; i<n; i++){
        sum=sum+arr[i];
    }
    return sum;
}
bool isPossible(vector<int>arr,int n,int m,int mid){
    
    int time=0;
    int painter=1;
    for(int i=0; i<n; i++){
        if(time+arr[i]<=mid){
            time=time+arr[i];
        }
        else{
            painter++;

            if (painter>m || arr[i]>mid){
                return false;
            }


            time=arr[i];
        }
    }
    return true;
}


int findLargestMinDistance(vector<int> &boards, int k)
{
        int n=  boards.size();
        int start=0;
        int end=sumOfArr(boards,n);
        int mid=start+(end-start)/2;

        int ans=-1;
        while(start<=end){
            if (isPossible(boards,n,k,mid)){
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