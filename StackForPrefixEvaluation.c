//The program evaluates given prefix expression using a stack
//The program assumes that each operand is a single digit integer
//The program is not meant to check the input expression nor 
//is it able to handle errors
//Example:
//1. -+7*45+20 = 25
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
//top=number of elements in stack-1
struct Stack
{
    int top;
    unsigned int size;
    int* arr;
};
struct Stack* create(unsigned size)
{
    struct Stack* stack=(struct Stack*)malloc(sizeof(struct Stack));
    stack->size=size;
    stack->top=-1;
    stack->arr=(int*)malloc(stack->size*sizeof(int));
    return stack;
}
int isFull(struct Stack* stack)
{
    return stack->top==stack->size-1;
}
int isEmpty(struct Stack* stack)
{
    return stack->top==-1;
}
void display(struct Stack* stack)
{
    if(isEmpty(stack)==-1) printf("Stack is empty!");
    else
    {
        printf("\nStack:");
        for(int i=0;i<=stack->top;i++)
            printf("\t%d",*(stack->arr+i));
    }
}
void push(struct Stack* stack, int item)
{
    if(isFull(stack))
        return;
    stack->arr[++stack->top]=item;
}
int pop(struct Stack* stack)
{
    if(isEmpty(stack))
        return -1;
    return stack->arr[stack->top--];
}
int peek(struct Stack* stack)
{
    if(isEmpty(stack))
        return INT_MIN;
    return stack->arr[stack->top];
}
int evaluatePrefix(char s[])
{
    int size=strlen(s);
    struct Stack* stack=create(size);
    int i;
    for(i=size-1;i>=0;i--)
        if(s[i]>='0' && s[i]<='9')  
            push(stack,s[i]-'0');
        else
        {
            int op1=pop(stack);
            int op2=pop(stack);
            switch(s[i])
            {
                case '+': push(stack,op1+op2); break;
                case '-': push(stack,op1-op2); break;
                case '*': push(stack,op1*op2); break;
                case '/': push(stack,op1/op2); break;
            }
        }
    return peek(stack);
}
void main()
{
    int ans=evaluatePrefix("-+7*45+20");
    printf("\nResult of evaluated prefix expression: %d",ans);    
}
