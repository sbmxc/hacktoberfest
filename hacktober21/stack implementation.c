#include<stdio.h>

#define SIZE 5

 typedef struct 
{
	int top;
	int s[SIZE];
}stack;

int IsEmpty(stack *);
int IsFull(stack *);
void push(stack *,int);
int pop(stack *);
int peep(stack *);
int Display(stack *);

int main()
{
	 stack st;
	st.top=-1;
	int x,ch,ele;

do{
	printf("\n 1. PUSH");
	printf("\n 2. POP");
	printf("\n 3. PEEP");
	printf("\n 4. DISPLAY");
	printf("\n 5. QUIT");

   printf("\n Enter a choice which you want");
   scanf("%d",&ch);
   
   switch(ch)
   {
   	
   	case 1: printf("\n Enter a element which you want to push");
   	         scanf("%d",&ele);
   	         push(&st,ele);
   	         break;
   	case 2: ele=pop(&st);
   	        if(ele==-1)
   	         printf("\n stack is empty");
   	         else
   	         printf("\n poped the element is=%d",ele);
   	         break;
   	case 3: ele=peep(&st);
   	         if(ele==-1)
   	         printf("\n stack is empty");
   	         else
   	         printf("\n peeped the element is=%d",ele);
   	         break;
   	case 4: Display(&st);
   	        break;
   	case 5: break;
   	default: printf("\n wrong choice! Try again");
   	         break;
   }
}while(ch!=5);
 return 0;
}
   	        
 int IsEmpty(stack*st)
 {
 	if(st->top==-1)
 	 return 1;
 	 else
 	 return 0;
}
 int IsFull(stack*st)
 {
 	if(st->top==SIZE-1)
 	return 1;
 	else
 	return 0;
}
void push(stack*st,int x)
{
	if(IsFull(st))
	{
		printf("stack is full");
	}
	else
	{
		st->top++;
		st->s[st->top]=x;
    }
}
int pop(stack*st)
{
	int x;
	if(IsEmpty(st))
	{
		return -1;
	}
	else
	{
		x=st->s[st->top];
		st->top--;
		return x;
    }
}
int peep(stack*st)
{
	int x;
	if(IsEmpty(st))
	 return -1;
	 else
	 {
	 	x=st->s[st->top];
	 	st->top--;
	 	return x;
	 }
}
int Display(stack*st)
{
	int i;
	for(i=st->top;i>=0;i--)
	printf("\n %d",st->s[i]);
	printf("\n");
}
