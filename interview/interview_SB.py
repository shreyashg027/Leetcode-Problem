# def countGroups(mat):
#
#     visited = [[False for j in range(len(mat[0]))] for i in range(len(mat))]
#     print
#     count = 0
#     lis = []
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if visited[i][j] == False and mat[i][j] == 1:
#                 count += 1
#                 DFS(i, j, visited, mat)
#                 # count += 1
#             lis.append(count)
#     return count
#
# def DFS(i, j, visited, mat):
#     rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
#     colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
#     visited[i][j] = True
#
#     for k in range(8):
#         if isSafe(i + rowNbr[k], j + colNbr[k], visited, mat):
#             DFS(i + rowNbr[k], j + colNbr[k], visited, mat)
#
# def isSafe(i, j, visited, mat):
#     return (i >= 0 and i < len(mat) and
#             j >= 0 and j < len(mat[0]) and
#             not visited[i][j] and mat[i][j])

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.sum = 0
        self.count = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        cluster = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count += 1
                    self.dfs(row, col,grid,cluster)

        return count,cluster

    def dfs(self, row, col, grid, cluster):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            if self.sum>0:
                cluster.append(self.sum)
            self.sum = 0
            return

        self.sum += grid[row][col]
        grid[row][col] = 0
        for r, c in [(0,1),(0,-1),(1,0),(-1,0)]:
            self.dfs(row + r, col + c, grid, cluster)

graph = [[1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0]]
test = Solution()
print(test.numIslands(graph))

