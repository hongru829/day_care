#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.55%)
# Total Accepted:    156.7K
# Total Submissions: 590.2K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i] == True:
                for j in xrange(i, (n-1)/i+1):
                    res[i*j] = False
        return sum(res)
   
