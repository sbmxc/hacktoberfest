#include<iostream>
using namespace std;


string Reverse(string str,int s,int n){
    if (s>n){
        return str;
    }
    
    char temp=str[s];
    str[s]=str[n];
    str[n]=temp;
    
    return Reverse(str,s+1,n-1);

}

int main()
{
    
    string l="abcde";
    int n=4 ;

    cout<<Reverse(l,0,n)<<endl;

    return 0;
}
