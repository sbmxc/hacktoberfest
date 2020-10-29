// https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem?

#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
        string array[9] = {"one","two","three","four","five","six","seven","eight","nine"};
    if(n>9){
        cout<<"Greater than 9";
    }
    else{
        cout<<array[n-1];
    }
}
