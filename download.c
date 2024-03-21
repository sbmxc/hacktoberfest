#include<stdio.h>
int main()
{
int M[10];
int j;
/* store seven numbers in array M */
 M[0] = 2;
 M[1] = 4;
 M[2] = 6;
 M[3] = 8;
 M[4] = 10;
 M[5] = 12;
 M[6] = 14;
/* print numbers in M */
 printf("Print all the Numbers : \n");
 for (j = 0; j < 7; ++j)
 printf("M[%d] = %d\n",j,M[j]);
/* print numbers in M backwards */
 printf("\nFrom End to Beginning : \n");
 for (j = 6; j >= 0; --j)
 {
 printf("M[%d] = %d\n",j,M[j]);
  }
}