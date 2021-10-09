#include<iostream>
using namespace std;
int findolder(int *a,int *b)
{
    if (*a>*b)
    {
        return *a;
    }
    else
    {
        return *b;
    }
}
int main()
{
    int a,b;
    cout<<"Enter first brother's age : ";
    cin>>a;
    cout<<"Enter second brother's age : ";
    cin>>b;
    cout<<"Brother with age "<<findolder(&a,&b)<<" is older.";
}