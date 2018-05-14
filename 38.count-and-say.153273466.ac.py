#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (36.94%)
# Total Accepted:    193.3K
# Total Submissions: 523.3K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# 
# 
# Given an integer n, generate the nth term of the count-and-say sequence.
# 
# 
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# Example 1:
# 
# Input: 1
# Output: "1"
# 
# 
# 
# Example 2:
# 
# Input: 4
# Output: "1211"
# 
# 
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        st = '1'
        if n == 1:
            return st
        for i in range(n-1):
            ret = ""
            count = 1
            for i in range(len(st)):
                try:
                    if st[i+1] == st[i]:
                        count += 1
                        continue
                except:
                    pass
                
                ret = ret + str(count) + st[i]
                count = 1
            st = ret
        return ret
    
        
