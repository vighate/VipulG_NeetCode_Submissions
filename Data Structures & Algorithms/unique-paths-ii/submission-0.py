class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        row = [0]*n
        row[n-1] = 1

        for i in range(m-1,-1,-1):
            newrow = [0]*n

            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    newrow[j] = 0
                elif j == n-1:
                    newrow[j] = row[j]
                else:
                    newrow[j] = newrow[j+1]+row[j]
            row = newrow
        return row[0]
