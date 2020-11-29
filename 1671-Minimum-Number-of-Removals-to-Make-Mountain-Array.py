# # 1671. Minimum Number of Removals to Make Mountain Array

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.


# Example 1:

# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove any elements.
# Example 2:

# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
# Example 3:

# Input: nums = [4,3,2,1,1,2,3,1]
# Output: 4
# Example 4:

# Input: nums = [1,2,3,4,4,3,2,1]
# Output: 1
 

# Constraints:

# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# It is guaranteed that you can make a mountain array out of nums.

# 思路: 先来一个Longest Increasing Sequence
# 再来一个 DP Array DP[i] 代表第i个位置上最长的increasing序列
# left_dp[nums] 代表从左边开始数
# right_dp[nums::-1] 代表从右边开始数
# 从i开始到n-1 遍历 从左边找到longest incresing sequence，再从右边找到 longest incresing sequence

# mll(max longest length) = max longest incresing sequence + max right longest increasing sequence
# return n - mll


# 还有另一种DP的方法是 用Binary Search的方法 时间复杂度是 O(nlogn)

# dp = []
# seq = []

# for num in nums:
#     index = bisect_left(seq, nums)

#     if index < len(seq):
#         seq[index] = num
#     else:
#         seq.append(num)
    
#     dp.append(len(seq))
#


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        def LIS(arr):
            n = len(arr)
            
            dp = [1] * n
            
            for i in range(1, n):
                for j in range(i):
                    if arr[j] < arr[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp
        
        n = len(nums)
        
        dp_left = LIS(nums)
        dp_right = LIS(nums[::-1])
        
        nmax = 0
        
        for i in range(n - 1):
            if dp_left[i] > 1 and dp_right[n - i - 1] > 1:
                nmax = max(nmax, dp_left[i] + dp_right[n - i - 1] - 1)
        
        return n - nmax