#include<stdio.h>
int main()
{
	int a=3,d=3,e=1,k,j;
	for(int i=1;i<=7;i++)
	{
		if(a>=0)
		{
			for(k=a;k>=1;k--)
			{
				printf(" ");
			}
			for(j=1;j<=i;j++)
			{
				printf("* ");
			}
	    	a--;
			printf("\n");
		}
		else
		{
			for(k=1;k<=e;k++)
			printf(" ");
			for(j=d;j>=1;j--)
			printf("* ");
			e++;
			d--;
			printf("\n");
		}
	}
}
