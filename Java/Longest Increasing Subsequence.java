/******************************************************************************
Leet Code :300. Longest Increasing Subsequence
Link : https://leetcode.com/problems/longest-increasing-subsequence/
*******************************************************************************/

class Solution {
    public int lengthOfLIS(int[] nums) {
        int lis[] = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            lis[i]=1;
        }
        for(int i=1;i<nums.length;i++){
            for(int j=0;j<i;j++){
                if((nums[i]>nums[j]) && (lis[i]<= lis[j])){
                    lis[i] = 1+lis[j]; 
                }
            }
        }
        int len=lis[0];
        for(int i=1;i<lis.length;i++){
            if(lis[i]>len){
                len=lis[i];
            }
        }
        return len;
    }
}
/*********
Runtime: 57 ms, faster than 61.44% of Java online submissions for Longest Increasing Subsequence.
Memory Usage: 41.8 MB, less than 38.70% of Java online submissions for Longest Increasing Subsequence.
*********/
