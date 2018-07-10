#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (30.76%)
# Total Accepted:    49.6K
# Total Submissions: 161.1K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# Example 1:
# 
# 
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
# 
# 
# Example 2:
# 
# 
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# 
# Example 3:
# 
# 
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# 
# Example 4:
# 
# 
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# 
# 
# Example 5:
# 
# 
# Input: num = "3456237490", target = 9191
# Output: []
# 
# 
#
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.helper(num, target, '', 0, 0)
        return self.res
    
    def helper(self, num, target, tmp, currRes, prevNum):
    
        if currRes == target and len(num) == 0:
            self.res.append(tmp)
            return
        
        for i in range(1,len(num) + 1):
            currStr = num[:i]
            currStrNum = int(num[:i])
            
            if len(currStr) > 1 and currStr[0] == '0':
                return
            
            nextStr = num[i:]
            
            if len(tmp)!= 0:
                self.helper(nextStr, target, tmp + '*' + currStr, (currRes - prevNum) + (prevNum * currStrNum), prevNum * currStrNum)
                self.helper(nextStr, target, tmp + '+' + currStr, currRes + currStrNum, currStrNum)
                self.helper(nextStr, target, tmp + '-' + currStr, currRes - currStrNum, -currStrNum)
            else:
                self.helper(nextStr, target, currStr, currStrNum, currStrNum)
                
            
            
            
            
            
        
