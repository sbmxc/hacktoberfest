public class LongestPalinSubstring {
   
    // This function prints the
    // longest palindrome substring
    // (LPS) of str[]. It also
    // returns the length of the
    // longest palindrome
    static int longestPalSubstr(String str)
    {
        int n = str.length(); // calculating size of string
        if (n < 2)
            return n; // if string is empty then size will be 0.
                  // if n==1 then, answer will be 1(single
                  // character will always palindrome)
 
        int maxLength = 1,start=0;
        int low, high;
        for (int i = 0; i < n; i++) {
            low = i - 1;
            high = i + 1;
            while ( high < n && str.charAt(high) == str.charAt(i)) //increment 'high'                                  
                high++;
       
            while ( low >= 0 && str.charAt(low) == str.charAt(i)) // decrement 'low'                   
                low--;
       
            while (low >= 0 && high < n && str.charAt(low) == str.charAt(high) ){
                  low--;
                high++;
        }
 
        int length = high - low - 1;
        if (maxLength < length){
            maxLength = length;
            start=low+1;
        }
    }   
    System.out.print("Longest palindrome substring is: ");
    System.out.println(str.substring(start, start + maxLength ));
    return maxLength;
       
 }
 
    // Driver program to test above function
    public static void main(String[] args)
    {
 
        String str = "forgeeksskeegfor";
        System.out.println("Length is: "
                           + longestPalSubstr(str));
    }
}
