// Problem-
//     string:"abc"
//     subsequence:{"","a","ab","abc","bc"}
//      print the longest common subsequence in strings s1 and s2

// Approach-
    // if s1[m-1]==s2[n-1]  ->  dp[m][n] = 1 + dp[m-1][n-1]
    // else   ->                dp[m][n] =  max( dp[m][n-1] , dp[m-1][n] )

// Time Complexity: O(N*M)
// Reason: There are two nested loops

// Space Complexity: O(N*M)
// Reason: We are using an external array of size ‘N*M’

import java.util.*;

class LCS{
static void lcs(String s1, String s2) {
    
    int n=s1.length();
    int m=s2.length();

    int dp[][]=new int[n+1][m+1];
    for(int i=0;i<=n;i++){
        dp[i][0] = 0;
    }
    for(int i=0;i<=m;i++){
        dp[0][i] = 0;
    }
    
    for(int ind1=1;ind1<=n;ind1++){
        for(int ind2=1;ind2<=m;ind2++){
            if(s1.charAt(ind1-1)==s2.charAt(ind2-1))
                dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1];
            else
                dp[ind1][ind2] = 0 + Math.max(dp[ind1-1][ind2],dp[ind1][ind2-1]);
        }
    }
    
    int len=dp[n][m];
    int i=n;
    int j=m;
    
    int index = len-1;
    String str="";
    for(int k=1; k<=len;k++){
        str +="$"; // dummy string
    }
    StringBuilder ss= new StringBuilder(s1);
    StringBuilder str2=new StringBuilder(str);
    while(i>0 && j>0){
        if(ss.charAt(i-1) == s2.charAt(j-1)){
            str2.setCharAt(index,ss.charAt(i-1) ); 
            index--;
            i--;
            j--;
        }
        else if(ss.charAt(i-1)>s2.charAt(j-1)){
            i--;
        }
        else j--;
    }
    System.out.println(str2);
}

public static void main(String args[]) {

  String s1= "abcde";
  String s2= "bdgek";
                                 
  System.out.print("The Longest Common Subsequence is ");
  lcs(s1,s2);
}
}