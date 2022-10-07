#include<bits/stdc++.h>

using namespace std;
int dp[1001][1001];

int wildcard(string p, string s, int i, int j){
    if(i==-1 and j==-1)
        return 1;
    if(j==-1){
        for(int k=0;k<i;k++){
            if(p[k]!='*')
                return 0;
        }
        return 1;
    }
    if(i==-1)
        return 0;
    if(dp[i][j]!=-1)
        return dp[i][j];
    if(p[i]==s[j] or p[i]=='?')
        return dp[i][j] = wildcard(p,s,i-1,j-1);
    if(p[i]=='*'){
        int res1 = wildcard(p,s,i-1,j);
        int res2 = wildcard(p,s,i,j-1);
        return dp[i][j] = res1 or res2;
    }
    return dp[i][j] = 0;
}

int main(){

    int t;
    cin>>t;
    while(t--){
        string p,s;
        cin>>p>>s;
        memset(dp,-1,sizeof(dp));
        int ans = wildcard(p,s,p.length()-1,s.length()-1);
        if(ans==1)
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }
    return 0;
}