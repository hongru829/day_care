


# longest consecutive sequence

# dp[i] means in the position i-1 the length of longest consecutive subsequence



def getLongestConsecutuiveSubsequence(self, nums):

    # 1, 4, 3, 8

    dp = [0 for _ in range(len(nums))]
    dp[0] = 1

    length = [0 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                maxRes = max(maxRes, dp[i])

    return maxRes





import Collections
def removeInvalidParenters(self, s):
    deQueue = Collections.deque

    deQueue.append(s)
    result = []
    visited = set()
    isStop = False

    while queue:

        size = len(queue)

        for k in range(len(size)):
            currentStr = queue.pop()

            if self.checkValid(currentStr):
                isStop == True
                res.append(currentStr)

            if isStop:
                break
            for i in range(currentStr):
                if currentStr[i] == ')' or currentStr[i] == '(':
                    nextStr = currentStr[:i] + currentStr[i+1:]

                    if nextStr not in visited:
                        deQueue.appendLeft(nextStr)
                        visited.add(nextStr)

    if len(result) == 0:
        return [""]
    else:
        return result

def checkValid(self, s):
    counter = 0
    for i in range(len(s)):
        if counter < 0:
            return False
        if s[i] == '(':
            counter += 1
        else:
            counter -= 1
    return counter == 0



def maxBinarySearchTree(self, root):


    self.res = float('-inf')
    self.temp = 0



    dfs(root):
        if root is None:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        self.temp = max(left + root.val, right + root.val)
        self.res = max(self.res, self.temp, root.val + left + right)

        reru








def maxPathOnBinarySearchTree(self, root)


    self.res = float('-inf')

    dfs(root):


        left = dfs(root.left)
        right = dfs(root.right)

        self.temp = max(left + root.val, right + root.val, root.val)
        self.res = max(self.res, temp, left + right + root.val)


        return self.res






def findAllAnagramsinString(String s,String p):

    dic1,dict2 = dict(), dict()

    for i in range(len(p)):
        dic1 = dict1.get(p[i],0) + 1

    start, end = 0,0

    while end < len(s):

        dict2 = dict2.get(s[end], 0) + 1

        if dic1 == dic2:
            res.append(start)

        if end - start + 1 > len(p):
            dic2[s[start]] -= 1
            if dict2[s[start]] == 0:
                del(dic2[s[start]])
            start += 1
    return res

def groupAnagram(self, strs):

    map = {}

    for str in strs:
        target = ''.join(sorted(str))

    if target not in map:
        map[target] = [v]

    else:
        map[target].append(v)

    for value in map.values():
        res += [value]

def numberofIslands(self, nums):













def courseSchedule(self, numCourses, prerequistes):


    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    for x,y in prerequistes:
        graph[x].append(y)

    def dfs(i)

        if visited[i] == -1:
            return False

        if visited[i] == 1:
            return True

        visited[i] =  -1
        for i in range(numCourses):
            if not dfs(i):
                return False
        visited[i] = 1
        return True


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0
        h = self.getHeight(nestedList)
        res = self.getSum(nestedList, h)
        return res

    def getHeight(self, nestedList):

        if nestedList is None or len(nestedList) == 0:
            return 0
        height = 0
        for l in nestedList:
            if l.isInteger():
                height = max(height, 1)
            else:
                height =  max(height, self.getHeight(l.getList()) + 1)
        return height

    def getSum(self, nestedList, layer):
        _sum = 0
        for l in nestedList:
            if l.isInteger():
                _sum += l.getInteger() * layer
            else:
                _sum += self.getSum(l.getList(), layer - 1)
        return _sum

























def 4sum(self, nums):

    left = 0
    right = len(nums) - 1
    res = []

    nums = sorted(nums)

    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j != i + 1 and nums[j] == nums[j-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[j] + nums[left] + nums[right]

                if temp == target:
                    res.append([i, j, left, right])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                if temp < target:
                    left += 1
                if temp > target:
                    right -= 1
    return res


def validPalindrom(s):

    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            l += 1

        while left < right and not s[right].isalnum():
            r += 1

        if s[left] != s[right]:
            return False
        l += 1
        r -= 1
    return True


def wordBreak(s, wordDict):

    for i in range(len(s) + 1):
        for j in range(0, i):
            if dp[j] and s[j:i] in wordDict:
                possible[i] = True
                break;

    return possible[sLen]


def wordBeak2(s, wordDict):


    def dfs(s, wordDict, dp, res, temp):

        if len(s) == 0:
            res.append(temp)

        for i in range(len(s)):

            if dp[i]:
                temp.append(s[:i+1]):
                dfs(s[i:], wordDict, dp, res, temp):















def maximumPathSum(self, root):


    self.total = 0



def pathSumHelper(self, root):
    left = pathSumHelper(self, root.left)
    right = pathSumHelper(self, root.right)
    temp = max(left + root.val, right + root.val, root.val)

    self.total = max(left + right + root.val, temp. self.total)
    return temp










def isSameTree(p, q):

    if p and q:
        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    else:
        p == q

def isSameTree(p, q):

    queue =  []
    queue.append([p, q])

    while queue:

        node1, node2 = queue.pop(0)

        if not node1 and not node2:
            continue

        elif None in [node1, node2]:
            return False

        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True

def constructTree(preorder, inorder):
        root = Node(preorder[0])
        rootPos = inorder.index(preorder[0])

        root.left = self.constructTree(preorder[1: 1 + rootPos], inorder[:rootPos])
        root.right = self.constructTree(preorder, inorder[rootPos+1:])
        return root

def balancedBSt(root):


    left = self.Depth(root.left)

    right = self.Depth(root.right)

    if left == -1 or right == -1 or Math.abs(left - right) < 1:
        return -1

    return max(left, right)



def Depth(root):

    if root == null:
        return 0

    return max(self.Depth(root.left), self.maxDepth(root.right)) + 1


def populate(self, root):

    stack = []

    queue = [root]

    while stack:

        queue = len(stack):

        for i in range(len(size)):

            if i < size - 1:
                node.next = stack[0]

            else:
                node.next = none

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

def pascals(numRows)

    numRows = [[1]* (i + 1) for i in range(numRows)]

    for i in numRows:
        for j in len(1, i):
            pascals[i][j] = pascals[i-1][j] + pascals[i-1][j-1]

    return pascal


def bestTimeTosellStock(prices):

    f1 = [0] * (len(prices) + 1)

    f2 = [0] * (len(prices) + 1)


    minPrice = prices[0]
    for i in range(1, len(prices)):
        minPrice = min(prices[i], minPrice)
        f1[i] = max(f[i-1], prices[i] - minPrice)

    maxPrice = prices[len(prices) - 1]
    for i in range(len(prices) - 2, -1, -1):
        maxPrices = min(prices[i+1], maxPrices)
        f2[i] = max(maxPrices - prices[i], maxPrices)

    res = 0
    for i in len(f1):
        if f1[i] + f2[i] > res:
            res = f1[i] + f2[i]
    return res


























