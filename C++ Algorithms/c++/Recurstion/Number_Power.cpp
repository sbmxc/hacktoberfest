#include<iostream>
using namespace std;

int Power(int n, int p){

    if(p==0){return 1;}
    if(p== 1){return n;}

    int ans=Power(n,p/2);

    if(p%2==0){
        return ans*ans;
    }
    else{
        return n*ans*ans;
    }
    



}

int main()
{
    cout<<Power(2,10)<<endl;

    return 0;
}
