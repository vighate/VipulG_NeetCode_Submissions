class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = [float('inf')]*(n+1)
        row[n-1] = 0
                
        for i in range(m-1,-1,-1):
            newrow = [float('inf')]*(n+1)
            for j in range(n-1,-1,-1):
                newrow[j] = grid[i][j] + min(newrow[j+1], row[j])
            row = newrow
        return row[0]
