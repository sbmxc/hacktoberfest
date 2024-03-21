class Solution {
    public boolean isPalindrome(int x) {
        
        int original = x;
        int reversed = 0;
      
        
        while(x>0){
            reversed = (reversed * 10) + (x%10);
            x/=10;
        }
       
        if(reversed == original) {
           return true;
        }
        else {
            return false;
        }
        
    }
}
