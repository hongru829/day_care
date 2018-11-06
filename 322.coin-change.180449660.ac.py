#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (26.61%)
# Total Accepted:    96.6K
# Total Submissions: 363K
# Testcase Example:  '[1]\n0'
#
# 
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# 
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# 
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] means in the position when the amount is i, fewest number of coins
        # if k + coins[j] = i
        # dp[i] = min( dp[k] + 1, dp[k] )
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for k in range(len(coins)):
                if i >= coins[k]:
                    dp[i] = min(dp[i - coins[k]] + 1, dp[i])
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
        
                

                
        
                
        
