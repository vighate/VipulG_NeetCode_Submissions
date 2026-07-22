class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        


        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}

        def dfs(r,c,length):

            if (r<0 or r>=rows or
                c<0 or c>=cols or matrix[r][c] <= length):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            value = matrix[r][c]
            dp[(r,c)] = 1+max(
                dfs(r,c+1,value),
                dfs(r+1,c,value),
                dfs(r,c-1,value),
                dfs(r-1,c,value)
            )

            return dp[(r,c)]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
               res = max(res, dfs(r,c,float('-inf')))
        return res