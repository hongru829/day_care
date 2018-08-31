

# 第一轮

# insert a number in ordered array

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid

        # print left
        # print right

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[left] < target < nums[right]:
            return right
        if target < nums[left]:
            return left - 1 if left > 0 else 0
        if target > nums[right]:
            return right + 1

# follow up 如果有 duplicate
        while left + 1 < right:
            mid = (left + right) / 2

            if nums[mid] == target:
                right = mid



# find the center of mass in a 2D array.


# delete node in a doubly linked list

import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    def deleteNode(self, dele):

        # base case
        if self.head is None or dele is None:
            return

        # if node to be deleted is head node
        if self.head = dele:
            self.head = dele.next


        # change next only f node to be deleted is not the last node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # change prev only‘



# 闲话不说，上面经：
# 前两天面的。三哥面试官
# 面试开始，直接上题。给了一个Quack的类，里面有三个方法：
# pop(): 随机从头或者尾扔出一个元素；
# peek(): 随机看头或者尾的一个元素，peek()之后pop()的话一定会pop()出peek()的那
# 个元素；
# push()：向尾部插入一个元素

# 问题是：给一个排序好的Quack,怎么把里面的元素原封不动的放到一个Array里面。
# follow-up：如果quack里面有重复的元素，怎么处理


# 在这里其实可以总结一下deque还包括deque的方法

Class Quack(object):

    def __init__(self):
        self.queue = collections.deque()
        pass

    def pop():
        res = 0
        random = _last_peek == -1 ? rand() % 2 : _last_peek
        if random == 0:
            res = queue.popleft()
            return res
        else:
            res = queue.pop()
            return res
        _last_peek = -1

    def peek():
        res = 0
        if rand() % 2 == 0:
            res = queue.peek()
            _last_peek = 0
        else:
            res = queue.peekfront()
            _last_peek = 1
        return res

    def push():
        self.queue.append(ele)





















