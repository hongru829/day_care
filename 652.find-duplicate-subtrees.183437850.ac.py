# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        m = collections.defaultdict(int)
        res = []
        self.dfs(root, m, res)
        return res
        
    def dfs(self, root, m, res):
        if root is None:
            return '#'
        path = str(root.val) + "," + self.dfs(root.left, m, res) + "," +  self.dfs(root.right, m, res)

        if m[path] == 1:
            res.append(root)
        m[path] += 1
        return path
