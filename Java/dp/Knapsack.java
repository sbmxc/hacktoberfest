// Problem-
// Given N items where each item has some weight and profit associated with it and also given a bag with capacity W,
// [i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag 
// such that the sum of profits associated with them is the maximum possible. 

// Approach
// dp[ind][cap] =  max(dp[ind-1][cap] ,dp[ind-1][cap-wt[ind]]

// Time Complexity: O(N*W)
// Reason: There are two nested loops

// Space Complexity: O(N*W)
// Reason: We are using an external array of size ‘N*W’.




import java.util.*; 
class Knapsack {

	static int knapSack(int W, int wt[], int val[], int n) 
	{ 
		
		int[] dp = new int[W + 1]; 

		for (int i = 1; i < n + 1; i++) { 
			for (int w = W; w >= 0; w--) { 

				if (wt[i - 1] <= w) 

					// Finding the maximum value 
					dp[w] = Math.max(dp[w], dp[w - wt[i - 1]] + val[i - 1]); 
			} 
		} 
		return dp[W]; 
	} 


	public static void main(String[] args) 
	{ 
		int profit[] = { 60, 100, 120 }; 
		int weight[] = { 10, 20, 30 }; 
		int W = 50; 
		int n = profit.length; 
		System.out.print(knapSack(W, weight, profit, n)); 
	} 
} 


