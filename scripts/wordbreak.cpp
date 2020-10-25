//word break 
#include<bits/stdc++.h>
using namespace std;
#define pb          push_back
#define m_p			make_pair
#define rep(i,a,b)	for(int i=a;i<b;i++)
#define sz(x)       (int)x.size()
#define f			first
#define s			second
#define debug		cout<<"##########3"<<endl
#define mod			1000000007
#define ll			long long

//Top Down
bool wordBreak(string s, vector<string> &dictV) {
    unordered_set<string> dict(dictV.begin(), dictV.end());
    	vector<int> words(s.length()+1);
    	words[s.length()]=1;
	for(int i=s.length()-1;i>=0;i--){
		for(int j=i+1; j<=s.length(); j++) {
                    if (dict.find(s.substr(i, j - i)) != dict.end()) {
                    	if(words[j])
                    		words[i]=true;
                    }
                }	
	}	    
		    
         return words[0]; 
}

string s,t;

int main() {
    ios::sync_with_stdio(false);
    cin.tie();
    cout.tie();
    int i,j,k,x,y,n,m,c=0,ans=0,le;
	vector<string> dict;	
	cin>>n;
	rep(i,0,n){
		cin>>s;
		dict.pb(s);
	}
	cin>>s;
	cout<<wordBreak(s,dict);
	return 0;
}
