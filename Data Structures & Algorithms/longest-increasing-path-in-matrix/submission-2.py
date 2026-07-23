class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}
        def dfs(r,c,pre):

            if (r<0 or r>=rows or c<0 or c>=cols or matrix[r][c] <= pre):
                return 0
        
            if (r,c) in dp:
                return dp[(r,c)]
            
            value = matrix[r][c]
            dp[(r,c)] = 1+max(
                dfs(r+1,c,value),
                dfs(r,c+1,value),
                dfs(r,c-1,value),
                dfs(r-1,c,value)
                )
            
            return dp[(r,c)]

        res = 0

        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j,float('-inf')))
        
        return res

