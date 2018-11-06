

def maximumSubarraySizeEqualsToK(nums, k):

    sum = {}
    cur_sum = 0
    maxLen = 0
    for i in xrange(len(nums)):
        cur_sum += nums[i]

        if cur_sum == k:
            maxLen = i + 1

        if cur_sum - k in sum:
            maxLen = max(maxLen, i -  sum[cur_sum])

        sum[cur_sum]

# binary tree iterator

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.cur = root


    def hasNext(self):
        """
        :rtype: bool
        """
        # 这种情况 还没有调用next的时候 栈是空的 但是 self.cur不是空的
        return self.stack or self.cur


    def next(self):
        """
        :rtype: int
        """
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        self.cur = self.stack.pop()
        node = self.cur
        self.cur = self.cur.right

        return node.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
