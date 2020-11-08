#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.12%)
# Total Accepted:    156.5K
# Total Submissions: 537.4K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    
    # 1 2 3 4 5 
    # 1 2 3 5 4
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1 2 3 4 5， 下一个是 1，2，3，5，4
        # 1，2，4，3，5 下一个是 1，2，4，5，3
        # 要让这个number变大, 降序的数字不管用 比如 8，7，6，5
        # 必须从右边找到第一个升序的序列,然后调从右到左找到第一个比index数大的数调换一下位置，后面的number从小到大排列 
        # 然后调从右到左找到第一个比index数大的数调换一下位置 为什么是这样呢，因为开始就是从右边往左边找，找到一个第一个
        # 开始升序的，说明后面的数都是降序的， 如果后面降序的数，比index数大 说明这是后面所有的数第一个比该数大的
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index = i - 1
                break
        if index == -1:
            nums.reverse()
        else:
            #which means the number will like this way: 5,4,3,2,1 -> 1,2,3,4,5
            for i in range(len(nums)-1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break

            nums[index + 1:len(nums)]=nums[index + 1 : len(nums)][::-1]
        
