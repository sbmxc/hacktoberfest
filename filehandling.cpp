#include <stdio.h>
int main(void){
   FILE *program;
   char ch;
   program = fopen(__FILE__, "r");
   do{
      ch=fgetc(program);
      printf("%c", ch);
   }
   while(ch!=EOF);
      fclose(program);
   return 0;
}
