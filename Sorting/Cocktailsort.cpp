/*
 * C Program to Implement CockTail Sort
 */
#include <stdio.h>
#define MAX 4
 
int main()
{
    int data[MAX];
    int i, j, n, c;
 
    printf("\nEnter the data");
    for (i = 0; i < MAX; i++)
    {
        scanf("%d", &data[i]);
    }
    n = MAX;    
    do
    {
        /*
          * Rightward pass will shift the largest element to its correct place at the end
         */
        for (i = 0;  i < n - 1; i++)
        {
            if (data[i] > data[i + 1])
            {
                data[i] = data[i] + data[i + 1];
                data[i + 1] = data[i] - data[i + 1];
                data[i] = data[i] - data[i + 1];
 
            }
 
        }
        n = n - 1;
        /* 
          * Leftward pass will shift the smallest element to its correct place at the beginning
          */
        for (i= MAX - 1, c = 0; i >= c; i--)
        {
            if(data[i] < data[i - 1])
            {
                data[i] = data[i] + data[i - 1];
                data[i - 1] = data[i] - data[i - 1];
                data[i] = data[i] - data[i - 1];
            }
        }
        c = c + 1;
 
    } while (n != 0 && c != 0);
    printf("The sorted elements are:");
    for (i = 0; i < MAX; i++)
    {
        printf("%d\t", data[i]);
    }
}
