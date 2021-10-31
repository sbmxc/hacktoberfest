/*   This is just a sum of digitd calculating program for a 5 digit number  */
#include<stdio.h>
#include<conio.h>
void main()
{
    int n,sum; sum=0;
    printf("\n Enter the number");
    scanf("%d",&n);
    int i;
    while(n>0)
    {
        i=n%10;
        sum=sum+i;
        n=n/10;
    }
  
    printf("\n The sum of the digits is %d",sum);
    getch();
}
