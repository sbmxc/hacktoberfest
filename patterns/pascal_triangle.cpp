#include<iostream>
using namespace std;
// 1
// 1 1
// 1 2 1
// 1 3 3 1
// 1 4 6  4 1
 int fact(int n){
        int factorial=1;
      for (int i=2; i<=n;i++){
          
      factorial= factorial*i;
       
    }
    return factorial;

 }



int main(){

int n;
cout<<" enter the number of columns: "<<endl;
cin>>n;

// int r;
// cout<<" enter the number of rows: "<<endl;
// cin>>r;

for (int i=0; i<n;i++){
    for (int j=0;j<=i;j++){
    cout<<fact(i)/(fact(j)*fact(i-j))<< " ";    //for int i=0 cout will be printed 1 time
    }                                           //int i=1; cout 2 times
    cout<<endl;
}


return 0;
}