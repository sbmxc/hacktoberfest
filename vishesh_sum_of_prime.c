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

checkPrime(int a){int c=0;
	for(int i=2;i<a;i++){
		if((a%i)==0)
		c++;
	}if(c>0)
return 0;
else
return 1;
}
