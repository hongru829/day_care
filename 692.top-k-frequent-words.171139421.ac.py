#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (42.07%)
# Total Accepted:    28.2K
# Total Submissions: 67K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
# 
# Example 1:
# 
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# 
# Example 2:
# 
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# 
# 
# 
# Follow up:
# 
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# 
#
class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __cmp__(self, other):
        if self.freq != other.freq:
            return cmp(self.freq, other.freq)
        else:
            return cmp(other.word, self.word)

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, FreqWord(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap).word for _ in xrange(k)][::-1]    
