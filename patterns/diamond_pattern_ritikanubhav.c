#include<stdio.h>
#include<math.h>

/*
     PATTERN

        * 
      * * * 
    * * * * *
      * * * 
        * 

*/

int main()
{
    int a;
    printf("Enter a size for the diamond (odd no preffered)\n");
    scanf("%d",&a);
    int spaces=a-1,temp,stars;
    for(int i=0;i<a;i++) 
    {
        temp=abs(spaces);
        stars=a-temp;
        while(temp--)
            printf(" ");
        while(stars--)
            printf("* ");
        printf("\n");
        spaces-=2;
    }
    return 0;
}