/*
nnnnnnnnnnnn     nnnnnn
nnnnnn nnnnnn    nnnnnn
nnnnnn  nnnnnn   nnnnnn
nnnnnn   nnnnnn  nnnnnn
nnnnnn    nnnnnn nnnnnn
nnnnnn     nnnnnnnnnnnn
*/

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("n");
        }
        for(int j=0;j<i;j++){
            printf(" ");
        }
        for(int j=0; j<n; j++){
            printf("n");
        }
        for(int j=0; j<n-i-1; j++){
            printf(" ");
        }
        for(int j=0;j<n;j++){
            printf("n");
        }
        printf("\n");
    }

    return 0;
}
