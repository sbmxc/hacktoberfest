#include <stdlib.h>
#include <stdio.h>

void languageOptions(int selectedLanguage)
{
    switch(selectedLanguage)
    {
        case 1:
            printf("Hola Mundo!\n");
            break;
        case 2:
            printf("Olá Mundo!\n");
            break;
        case 3:
            printf("你好，世界!\n");
            break;
        case 4:
            printf("नमस्ते दुनिया!\n");
            break;
        case 5:
            printf("Bonjour le monde!\n");
            break;
        default:
            printf("Hello World!\n");
    }
}

int main()
{
    int selectedLanguage;
    printf("Hello World!\n\n");
    printf("1. Spanish\n");
    printf("2. Portuguese\n");
    printf("3. Chinese\n");
    printf("4. Hindi\n");
    printf("5. French\n\n");
    printf("Which language would you like to translate this message to? (Enter a number from 1-5): ");
    scanf("%d", &selectedLanguage);

    languageOptions(selectedLanguage);
    return 0;
}