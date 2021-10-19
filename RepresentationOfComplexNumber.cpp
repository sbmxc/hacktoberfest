#include<iostream>
#include<conio.h>
using namespace std;

class Complex
{
    int a,b,num;

    public:

    inline void display();

    Complex()
    {
        cout<<"Enter numbers to initialize a complex number : \n";
        cin>>a>>b;
        cout<<"Your Complex number : "<<a<<" + "<<"("<<b<<")"<<"i"<<endl;
    } 
    
    void add_real()
    {
      cout<<"Enter the number : ";
      cin>>num;
      a=a+num;
      cout<<"Added\n";
    }

    void subtract_real()
    { 
      cout<<"Enter the number : ";
      cin>>num;
      a=a-num;
      cout<<"Subtracted\n";
    }

    void add_imag()
    {
      
      cout<<"Enter the number : ";
      cin>>num;
      b=b+num;
      cout<<"Added.\n";

    }

    void subtract_imag()
    {
      
      cout<<"Enter the number : ";
      cin>>num;
      b=b-num;
      cout<<"Subtracted.\n";

    }

};

void Complex:: display()
{
    cout<<a<<" + "<<"("<<b<<")"<<"i"<<endl;
}



int main()
{ 
    cout<<"\n                              Manav Naharwal 05316401519\n\n";
    cout<<"\n\t       ----------------------------------------------------------------------\n";
	  cout<<"\t       R e p r e s e n t a t i o n     of     C o m p l e x     N u m b e r s\n";
	  cout<<"\t       ----------------------------------------------------------------------\n\n\n";
    Complex c;

    while(1)
    {
       int k;
       cout<<"\nWhat do you want to do :\n";
       cout<<"\n1.Display the complex number\n2.Add a real number to complex number\n3.Subtract a real number from complex number\n4.Add a imaginary number to complex number\n5.Subtract a imaginary number from complex number\n6.Exit\n\n";
       cin>>k;

       switch(k)
       {
         case 1:
         c.display();
         getch();
         break;
         
         case 2:
         c.add_real();
         getch();
         break;

         case 3:
         c.subtract_real();
         getch();
         break;

         case 4:
         c.add_imag();
         getch();
         break;

         case 5:
         c.subtract_imag();
         getch();
         break;

         case 6:
         return 0;

         default:
         cout<<"Wrong Input !";
         break;

       }
      
    } 
}