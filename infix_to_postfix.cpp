#include <iostream>
using namespace std;


class stack
{
    int arr[10];
    int top = -1;
    int n = 5;

public:
    // int start(int n)
    // {
    //     arr = new int[n];
    // }
    void size(){
        cout<< "@" <<n;
        cout<< endl;
    }
    void push()
    {
        if (top == n - 1)
        {
            cout << "stack overflow, can't add";
            cout << endl;
            return;
        }
        cout << "enter the element to be added"<<endl;
        int y;
        cin >> y;
        top++;
        arr[top] = y;
    }
    void pop()
    {
        if (top == -1)
        {
            cout << "No element to pop\n";
            return;
        }
        else
        {
            top--;
            cout<<"element popped\n";
        }
    }
    void peek()
    {
        cout << "enter the position to peek from current position: ";
        int x;
        cin >> x;
        if (x > (top + 1))
        {
            cout << "limit exceeded to peek\n";
            return;
        }
        else
        {
            cout << "the element from top at this position is: " << arr[top + 1 - x];
            cout<<endl;
        }
    }
    void is_empty()
    {
        if (top == -1)
        {
            cout << "the stack is EMPTY";
            cout << endl;
        }
        else if (top>-1 || top<n)
        {
            cout << "the stack is NOT COMPLETERLY EMPTY OR FULL";
            cout << endl;
        }
        else
        cout << "the stack is FULL";
        cout << endl;
    }
    void Top()
    {
        cout << "the current top is: " << top;
        cout << endl;
    }

};

int main()
{
    int x;
    stack s1;

    return 0;
}