# letcode

<h1>GRAPH</h1>

Clone Graph 这一道题我在用bfs做的时候, 考虑到需要创建一个queue(这个queue是通过[]来实现的),做bfs操作的时候， 我们必须要在尾部pop元素 然后新来的元素 要是放在头部
或者 在头部pop元素, 新来的元素放在后面 用的是 pop(0)的方法 很巧妙 pop最前面 append是加到list后面

```
核心代码
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
```


<h2>Yahoo Champion</h2>

Longest Rerepeated Substr
ing

<h2>Rubrik </h2>

[5,5,0,3,0,9]
-> 14
GOAL: to pick elements from array and return the greatest sum possible CONSTRAINTS
1. You cannot pick adjacent elements
2. You must pick elements that are increasing from left to right


定义dp[i] 包括nums[i]的时候 能取到的最大值， 每一个位置都计算一次最后取dp array里面最大的值

dp[i] could get from two ways

dp[i] = max(dp[0,1, ...i - 1]) + nums[i]) (nums[0,... i - 1] < nums[i]) || nums[i]

```

def getMaxSum(self, num):

	for i in range(len(nums)):
    	for j in range(i - 1):
        	if nums[j] > nums[i]



def getMaxSum(self, nums)
    if nums is None or len(nums) == 0:
        return 0
#   [100,5,9]
    dp = [0]* len(nums)

    dp[0] = nums[0]
    dp[1] = nums[1]
    #nums[2] > nums[0] dp[2] = dp[0] + nums[2]
    # dp[2] = nums[2]
    # nums =[100,1,0,200]
    # dp =  [100,1,0, 300]
    # dp[n] if nums[n] > max(nums[1..n-2]) dp[n] = max(dp[1...n-2]) + nums[n]     # else dp[n] =         #nums[n]

    for i in range(2, len(nums)):
        bestSum = 0
        for j in range(0, i):
            if nums[j] < nums[i]:
                bestSum = max(dp[j], bestSum)

        dp[i] =  bestSum + nums[i]

    return max(dp)
```


4sum 3sum的问题

比较值得注意的是, i, j, left, right 是怎么设定的

for i in range(len(nums))
    for j in range(i+1, len(nums))

        left = j + 1
        right = len(nums) - 1
        while left  < right







```
public

```
