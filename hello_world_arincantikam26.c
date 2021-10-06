#include <stdio.h>

int main()
{
    
    char name[100];
    char choice[100];
    printf("Please, Enter Your Name : ");
    scanf("%s", &name);  
    printf("Hi %s",name);
    printf(" How are you? \n");
    printf("fine or no?");
    scanf("%s", &choice);
   
    if(choice=="%sno",choice){
        printf("Heii, fighting, you did well today!!");
    }else {
        printf("You did well, good job dear!!");
    }
    return 0;
}

