

#leetcode 49  Group Anagrams  https://leetcode.com/problems/group-anagrams/
#leetcode 270 Closest Binary Search Tree Value https://leetcode.com/problems/closest-binary-search-tree-value/description/
#leetcode 256

#leetcode 287
#leetcode 260
#leetcode 261 Graph Valid Tree



# leetcode number of island

# dfs method

def numberifIsland(self, grid):

    if grid is None or len(grid) == 0:
        return 0
    m, n = len(grid), len(grid[0])

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                self.dfs(grid, i, j, m ,n)
                count += 1
    return count

def dfs(grid, i, j, m, n):

    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1
        return

    grid[i][j] == '#'

    self.dfs(grid, i+1, j, m, n)
    self.dfs(grid, i-1, j, m, n)
    self.dfs(grid, i, j-1, m, n)
    self.dfs(grid, i, j+1, m, n)

# dfs iterative

class Solution:

    def numIslans(self, grid):
        m = len(grid)

        if m == 0:
            return 0

        visited = [[False for i in range(n)] for j in range(m)]

        def check(x,y):
            if x >=0 and x < m and y >= 0 and y < n and grid[x][y] and visited[x][y] == False
                return True

        def bfs(x ,y):
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            q = [(x, y)]

            while len(q) > 0:
                x = q[0][0]
                y = q[0][1]
                q.pop(0)
                for k in range(4):
                    newx


def groupAnagrams(self, strs):

    map = {}
    for i, v in enumerate(strs):

        target = "".join(sorted(v))

        if target not in map:
            map[target] = [v]
        else:
            map[target].append(v)
    result = []

    for value in map.values():
        result += [sorted(value)]

# two medthod
def cloestBinaryTree(self, root):

    self.res = root.val


def numberofIslands(self, grid):


    def check(grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i >= 0 and i < n and j >=0 and j <= n and visited[i][j] == False:
            return True


    def bfs(self, x, y):

        q = [(x, y)]
        directions = [[0,1], [0, -1], [-1, 0], [1, 0]]

        while q:
            posX = q[0][0]
            posY = q[0][1]
            q.pop()
            for dir in directions:
                newX = posX + dir[0]
                newY = posY + dir[1]
                if check(newX, newY):
                    visited[newX][newY] = True
                    q.append((newX, newY))
    count = 0

    for row in range(m)
        for col in range(n):
            if check(row, col):
                visted[row][col] = True
                bfs(row, col)
                count += 1
    return count






def closetBinaryTreeHelper(self, root, target, temp):

    if abs(root.val - target) < abs(res - root.val):
        self.res =
