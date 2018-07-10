/*
 * [673] Number of Longest Increasing Subsequence
 *
 * https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (31.91%)
 * Total Accepted:    17.9K
 * Total Submissions: 56K
 * Testcase Example:  '[1,3,5,4,7]'
 *
 * 
 * Given an unsorted array of integers, find the number of longest increasing
 * subsequence.
 * 
 * 
 * Example 1:
 * 
 * Input: [1,3,5,4,7]
 * Output: 2
 * Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1,
 * 3, 5, 7].
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: [2,2,2,2,2]
 * Output: 5
 * Explanation: The length of longest continuous increasing subsequence is 1,
 * and there are 5 subsequences' length is 1, so output 5.
 * 
 * 
 * 
 * Note:
 * Length of the given array will be not exceed 2000 and the answer is
 * guaranteed to be fit in 32-bit signed int.
 * 
 */
class Solution {
    public int findNumberOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int len = nums.length;
     int dp[] = new int[len];
    int length[] = new int[len];
        int maxLen = 0;
        // int count = 1;
        // length[0] = 1;
        // dp[0] = 1;
        for (int i = 0; i < len; i++) {
            length[i] = 1;
        }
        
        for (int i = 0; i < len; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                     
                    
                    // dp[i]  = Math.max(dp[j] + 1, dp[i]);
                    if (dp[j] >= dp[i]) {
                        length[i] = length[j] ;
                        dp[i] = dp[j] + 1;
                    }  else if (dp[j] + 1 == dp[i]){
                        length[i] += length[j];
                    }
                    

                }
            }
        maxLen = Math.max(dp[i], maxLen);
        }
        int count = 0;
        for (int i = 0; i < len; i++) {
            if (dp[i] == maxLen) {
                count += length[i];
            }
        }
        
            //     for (int j = 0; j < N; ++j) {
            // for (int i = 0; i < j; ++i) if (nums[i] < nums[j]) {
            //     if (lengths[i] >= lengths[j]) {
            //         lengths[j] = lengths[i] + 1;
            //         counts[j] = counts[i];
            //     } else if (lengths[i] + 1 == lengths[j]) {
            //         counts[j] += counts[i];
            //     }
            // }
        // }
        
        
        return count;
    }
    
//     class Solution {
//     public int findNumberOfLIS(int[] nums) {
//         int N = nums.length;
//         if (N <= 1) return N;
//         int[] lengths = new int[N]; //lengths[i] = length of longest ending in nums[i]
//         int[] counts = new int[N]; //count[i] = number of longest ending in nums[i]
//         Arrays.fill(counts, 1);

//         for (int j = 0; j < N; ++j) {
//             for (int i = 0; i < j; ++i) if (nums[i] < nums[j]) {
//                 if (lengths[i] >= lengths[j]) {
//                     lengths[j] = lengths[i] + 1;
//                     counts[j] = counts[i];
//                 } else if (lengths[i] + 1 == lengths[j]) {
//                     counts[j] += counts[i];
//                 }
//             }
//         }

//         int longest = 0, ans = 0;
//         for (int length: lengths) {
//             longest = Math.max(longest, length);
//         }
//         for (int i = 0; i < N; ++i) {
//             if (lengths[i] == longest) {
//                 ans += counts[i];
//             }
//         }
//         return ans;
//     }
// }
    
    
}
