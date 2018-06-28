#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (51.87%)
# Total Accepted:    61.1K
# Total Submissions: 117.8K
# Testcase Example:  '"USA"'
#
# 
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# 
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter,
# like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# Input: "USA"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase
# latin letters.
# 
#
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length = len(word)
        
        firstIsCaptial = word[0].isupper()
        i = 1
        hasLower = False
        hasCaptial = False
        
        while i < length:
            
            if word[i].islower():
                hasLower = True
            else:
                hasCaptial = True
            if hasLower and hasCaptial:
                return False
            i += 1
        
        if not firstIsCaptial and hasCaptial:
            return False
        
        return True
        
