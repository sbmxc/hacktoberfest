#include<stdio.h>
#include <time.h>


int fib(int n)
{
    if (n>0)
    {
        if (n==0)
        {
            return 0;
        }
        else if (n==1)
        {
            return 1;
        }
        else 
        {
            return (fib(n-1)+fib(n-2));
        }

    }
}

int main()
{
    clock_t start,end;
    double cpu_time_used;
    start=clock();
    int f,r;
    scanf("%u",&f);
    r=fib(f);
    end =clock();
    printf("Value = %u , Time = %ld \n",r,end - start);
    return 0;
}