/* This problem is about to make a full diamond pattern using c languge.*/
#include<stdio.h>
int main()
{
    int n,k,j,i;
    printf("Enter the row number:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(k=1;k<=n-i;k++)
        {printf(" ");}
            for(j=1;j<=2*i-1;j++)
            { 
                printf("*");
            }
       printf("\n"); }
    
    for(i=n-1;i>=1;i--)
    {
        for(k=1;k<=n-i;k++)
        {printf(" ");}
            for(j=2*i-1;j>=1;j--)
            {
                printf("*");
            }
        printf("\n");}
return 0;    
}   

/* Enter row NUmber:5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    
 */   
