#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int size =(n*2)-1;
    int arr[size][size],front=0,rear=size-1;
    while (n!=0)
    {
         for(int i=front;i<=rear;i++)
         {
             for(int j=front;j<=rear;j++)
             {
                 if(i==front || j==front || i==rear || j==rear)
                     arr[i][j]=n;
             }
         }
         front++; rear--; n--;
    }
    for(int i=0;i<size;i++)
    {
        for(int j=0;j<size;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
