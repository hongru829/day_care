

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
