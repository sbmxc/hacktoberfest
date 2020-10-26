#include <stdio.h>
void main() {
	int n, i, flag = 0;
	printf("Enter a positive integer : ");
	scanf("%d", &n);
	for (i = 2; i <= n/2; i++) {
		if (checkPrime(i) == 1) {
			if (checkPrime(n-i) == 1) {
				printf("%d = %d + %d\n", n, i, n - i);
				flag = 1;
			}
		}
	}
	if (flag == 0) {
		printf("%d cannot be expressed as the sum of two prime numbers\n", n);
	}
}
int checkPrime(int i)
{
	int j,b=0;
	for(j=2;j<=i-1;j++)
	{
		if(i%j==0)
		break;
		else
		b++;
		continue;
	}
	{
		if(b==i-2)
		return 1;
		else
		return 0;
	}

}
