// 1665. Minimum Initial Energy to Finish Tasks
// Hard

// 83

// 17

// Add to List

// Share
// You are given an array tasks where tasks[i] = [actuali, minimumi]:

// actuali is the actual amount of energy you spend to finish the ith task.
// minimumi is the minimum amount of energy you require to begin the ith task.
// For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

// You can finish the tasks in any order you like.

// Return the minimum initial amount of energy you will need to finish all the tasks.

 

// Example 1:

// Input: tasks = [[1,2],[2,4],[4,8]]
// Output: 8
// Explanation:
// Starting with 8 energy, we finish the tasks in the following order:
//     - 3rd task. Now energy = 8 - 4 = 4.
//     - 2nd task. Now energy = 4 - 2 = 2.
//     - 1st task. Now energy = 2 - 1 = 1.
// Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.
// Example 2:

// Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
// Output: 32
// Explanation:
// Starting with 32 energy, we finish the tasks in the following order:
//     - 1st task. Now energy = 32 - 1 = 31.
//     - 2nd task. Now energy = 31 - 2 = 29.
//     - 3rd task. Now energy = 29 - 10 = 19.
//     - 4th task. Now energy = 19 - 10 = 9.
//     - 5th task. Now energy = 9 - 8 = 1.
// Example 3:

// Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
// Output: 27
// Explanation:
// Starting with 27 energy, we finish the tasks in the following order:
//     - 5th task. Now energy = 27 - 5 = 22.
//     - 2nd task. Now energy = 22 - 2 = 20.
//     - 3rd task. Now energy = 20 - 3 = 17.
//     - 1st task. Now energy = 17 - 1 = 16.
//     - 4th task. Now energy = 16 - 4 = 12.
//     - 6th task. Now energy = 12 - 6 = 6.

class Solution(object):
#     def minimumEffort(self, tasks):
#         """
#         :type tasks: List[List[int]]
#         :rtype: int
#         """
#         tasks.sort(key=lambda x:(x[1] - x[0]), reverse = True)
        
#         ans = 0
#         cur_saved = 0
        
#         for actual,minimum in tasks:
#             if minimum > cur_saved:
#                 needed = minimum - cur_saved
#                 ans += needed
#                 cur_saved += needed
            
#             cur_saved -= actual
        
#         return ans
    
    # Binary Search 的做法
    # Binary Search 确定边界 left, right
    # left = sum(actuals...)
    # right = sum(minimums...)
    # helper function 就是check 某一个数字是否是合乎规定的
    # 
    
    def minimumEffort(self, tasks):
        
        def helper(mid):
            for actual, minimum in tasks:
                if mid - minimum < 0:
                    return False
                mid = mid - actual
            return True
            
        
        tasks.sort(key=lambda x: (x[1]-x[0]), reverse = True)
        
        left = sum([a for a,m in tasks])
        right = sum([m for a, m in tasks])

        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if helper(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
        
        