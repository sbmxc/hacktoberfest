#include <iostream>
#include <stack>
using namespace std;
    bool isValid(string s) {
        stack<char>st;
        for(auto i:s){
            if(i=='('||i=='{'||i=='['){
                st.push(i);
                
            }
            else{
                if(st.empty()||(i==')'&&st.top()!='(')||(i=='}'&&st.top()!='{')||(i==']'&&st.top()!='[')){
                   return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }

int main() {
   string expresion = "()[](){()}]";
   if (isValid(expresion))
      cout << "This is Balanced Expression";
   else
      cout << "This is Not Balanced Expression";
}