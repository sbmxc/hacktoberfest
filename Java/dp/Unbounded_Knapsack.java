// Problem-
//      A thief wants to rob a store. He is carrying a bag of capacity W. 
//      The store has ‘n’ items of infinite supply. Its weight is given by the ‘wt’ array and its value by the ‘val’ array.
//      He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction.We need to find the maximum 
//      value of items that the thief can steal. He can take a single item any number of times he wants and put it in his knapsack.

// Approach-
        // dp[ind][cap] =  max(dp[ind-1][cap] ,dp[ind][cap-wt[ind]]

// Time Complexity: O(N*W)
// Reason: There are two nested loops

// Space Complexity: O(N*W)
// Reason: We are using an external array of size ‘N*W’. Stack Space is eliminated.



import java.util.*;

class Unbounded_Knapsack {
    
    static int unboundedKnapsack(int n, int W, int[] val, int[] wt) {
        int[][] dp = new int[n][W + 1];

        // Base condition
        for (int i = wt[0]; i <= W; i++) {
            dp[0][i] = ((int) i / wt[0]) * val[0];
        }

        for (int ind = 1; ind < n; ind++) {
            for (int cap = 0; cap <= W; cap++) {

                //not taken
                int notTaken = 0 + dp[ind - 1][cap];
                int taken = Integer.MIN_VALUE;

                if (wt[ind] <= cap)
                    taken = val[ind] + dp[ind][cap - wt[ind]];

                dp[ind][cap] = Math.max(notTaken, taken);
            }
        }

        return dp[n - 1][W]; 
    }

    public static void main(String args[]) {
        int wt[] = { 2, 4, 6 };
        int val[] = { 5, 11, 13 };
        int W = 10;
        int n = wt.length;

        System.out.println("The Maximum value of items the thief can steal is " + unboundedKnapsack(n, W, val, wt));
    }
}
