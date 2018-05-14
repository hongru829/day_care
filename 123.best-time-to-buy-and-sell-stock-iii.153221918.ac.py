#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (30.49%)
# Total Accepted:    108.7K
# Total Submissions: 356.5K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 只允许做2次交易，解法很巧妙，开辟2个数组 f1 and f2 f1[i] 表示在 prices[i] 之前进行一次交易所获得的最大利润
        # f2[i]表示 在price[i] 之后进行一次交易所获得的最大利润 f1[i] + f2[i] 的最大值 就是所要求的最大值
        
        # 而 f1[1] f2[i] 的计算就需要动态规划
        
        length = len(prices)
        
        if length == 0:
            return 0
        
        f1 = [0 for i in range(length)]
        f2 = [0 for i in range(length)]
        
        minV = prices[0]
        f1[0] = 0
        for i in range(1, length):
            minV = min(minV, prices[i])
            f1[i] = max(f1[i-1], prices[i] - minV)
        
        
        maxV = prices[length-1]
        f2[length-1] = 0
        for i in range(length-2, -1, -1):
            maxV = max(maxV, prices[i])
            f2[i] = max(f2[i+1], maxV - prices[i])
        res = 0
        
        for i in range(length):
            if f1[i] + f2[i] > res:
                res = f1[i] + f2[i]
                
        return res
