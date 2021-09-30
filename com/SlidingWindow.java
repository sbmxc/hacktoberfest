
public class SlidingWindow {
    public static void main(String[] args) {
        int[] nums = { 1, 3, -1, -3, 5, 3, 6, 7 };
        int k = 3;
        int res = maxSubArray(nums, k);
        System.out.println(res);
    }

    public static int maxSubArray(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (i >= k - 1) {
                max = Math.max(max, sum);
                sum -= nums[i - k + 1];
            }
        }
        return max;
    }
}

// Time Complexity: O(n) Space Complexity: O(1)
