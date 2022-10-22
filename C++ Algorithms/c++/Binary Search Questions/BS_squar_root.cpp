#include <iostream>
using namespace std;


long long int SquarRoot_BS(int  number){

    int s=0;
    int e=number;
    int ans=-1;
    long long int mid=s+(e-s)/2;
    while(s<=e){
        
        if((mid*mid)==number){
            return number;
        }
        if((mid*mid)>number){
            e=mid-1;
            ans=mid;
        }
        else{
            ans=mid;
            s=mid+1;
        }
        mid=s+(e-s)/2;
        
        
    }
    return ans;
}


double MorePrecision(int n ,int precision ,int squarRoot ){// some extra stuff it is used to print in decimal

    double ans =squarRoot;
    double  factor=1;
    for(double x=0; x<precision; x++){
        factor=factor/10;
        for(double j=ans; j*j<n; j=j+factor){
            ans=j;
        }

    }
    return ans;
}


int main()
{   
    int number= 101;
    int sr=SquarRoot_BS(number);
    double mp=MorePrecision(number,3,sr);
    cout<<"Squar Root of "<< number <<" is "<< mp<<endl;






    return 0;
}
