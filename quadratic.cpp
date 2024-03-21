#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a,b,c,d;

    cout<<"Enter the quardratic coeficients"<<'\n';
    cin>>a>>b>>c;
    
    if(a==0 && b ==0 )
    {
        cout<<"Invalid coeficients";
        return 1;
    }
    else if(a == 0)
    {
        cout<<"Solution is "<<-c/b;
        return 0;
    }

    d = b*b - 4*a*c;

    if(d<0)
        cout<<"Roots are imaginary";
    else if(d == 0)
        cout<<"Root is "<<-b/2/a;
    else cout<<"Roots are "<<(-b + sqrt(d))/2/a<<" and "<<(-b - sqrt(d))/2/a;
    
    return 0;
}
