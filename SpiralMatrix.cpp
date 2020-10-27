class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
     
        vector<int> v;
        int i, k=0,l=0;
        int r= matrix.size();
        if(r==0) return v;
        int m=r-1;
        int c=r?matrix[0].size():0;
        int n=c-1;
        while(k<=m && l<=n)
        {
            for(i=l;i<=n;i++)                    //l is the column start, n is column end
                v.push_back(matrix[k][i]);      // k is the start row and m is the end row
            k++;
            for(i=k;i<=m;i++)
                v.push_back(matrix[i][n]);
            n--;
    
          if(m>=k){
            for(i=n;i>=l;i--)
                    v.push_back(matrix[m][i]);
             m--;}
          if(n>=l){
            for(i=m;i>=k;i--)
                   v.push_back(matrix[i][l]);
            l++;}
       }
        return v;
    }
};
