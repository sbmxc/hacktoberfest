#include<stdio.h>
#include<string.h>

int main(){
	char str[100];
	int i,n,flag=0,f=0;

	printf("-----Comment Check-------");
	printf("\nEnter any string: ");
	scanf("%[^\n]s",str);
	n=strlen(str);

	if(str[0]=='/' && str[1]=='/')
		printf("%s is a single line comment",str);
	else if((str[0]=='/' && str[1]=='*') && (str[n-1]=='/' && str[n-2]=='*'))
		printf("%s is a multi line comment",str);
	else{
		for(i=2;i<n-1;i++){
			if(str[i]=='/' && str[i+1]=='/'){
				printf("Given string contains single line comment");
				break;
			}
			if(str[i]=='/' && str[i+1]=='*'){
				f=1;
			}
			if(f==1){
				if(str[i]=='*' && str[i+1]=='/'){
					printf("Given string contains multiline comment");
					break;
				}
			}
		}
		if(!f)
		printf("No comment");
	}

	return 0;
}
