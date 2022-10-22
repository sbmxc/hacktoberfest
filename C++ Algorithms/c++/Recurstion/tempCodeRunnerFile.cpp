
void BubleSort(int* arr[],int s,int n){
    if(s>n){
        return ;
    }
    if(n==1 || n==0){
        return ;
    }

    if(arr[s]>arr[s+1]){
        swap(arr[s],arr[s+1]);
    }
    s++;
    BubleSort(arr,s,n);
