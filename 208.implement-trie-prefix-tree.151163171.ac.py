#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (31.23%)
# Total Accepted:    113.1K
# Total Submissions: 362K
# Testcase Example:  '["Trie","search"]\n[[],["a"]]'
#
# 
# Implement a trie with insert, search, and startsWith methods.
# 
# 
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
#
class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.children = dict()

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            
            currNode = currNode.children[c]
        currNode.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root
        
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        
        return currNode.isEnd
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currNode = self.root
        
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
