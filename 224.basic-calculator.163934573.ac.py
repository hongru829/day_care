#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (29.26%)
# Total Accepted:    70.9K
# Total Submissions: 242.4K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# Example 1:
# 
# 
# Input: "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = 1
        res = 0
        i = 0
        # 在python代码里面for循环改变i的值 并不会导致i的改变 但是 在java里面 却可以导致i的改变
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num*10 + int(s[i+1])
                    i += 1
                res += num * sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res = res* stack.pop() + stack.pop()
            i += 1
        return res
            
    
            
            
        
