
#include<stdio.h>
/*a program print the position of smallest number of n numbers using array */
int main()
{
    int a[100],i,n,small,pos;
    printf("enter the no of element");
    scanf("%d",&n);
    printf("enter the numbers");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    small=a[0];
    pos=0;
    for(i=1;i<n;i++)
    {
        if(small>a[i])
        {small=a[i];
        pos=i;}
    }
    printf("position of smallest number is %d",(pos+1));
}
