
leetcode 325: Maximum Size Subarray Sum Equals k


Union Find 用来发现联通分量

Union Find 在 redundant connection的应用 刚开始的时候 一个一个连
union(u, v) 在union的时候发现 u 和 V 有相同的 parent， 说明这一条边就是redundant的

Union Find 还可以解决number of island 那道题目

number of island dfs 做法， 写完的时候, 提交代码，遇到的错误是 超过了递归的
范围， 也就是内存爆了, 也就是相当于没有加下面一行代码， 下面一行代码其实就是
想当于加了一个visited的数组


```
grid[i][j] == '2':

```

```
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    print i,j
                    self.dfs(grid, i, j)
                    count += 1
        return count


    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '2':
            return
        grid[i][j] = '2'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
```
