class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        path = {}
        rows = len(matrix)
        cols = len(matrix[0])
        def dfs(r,c,pre):

            if (c<0 or c>=cols
                or r<0 or r>=rows 
                or matrix[r][c] <= pre):
                return 0

            if (r,c) in path:
                return path[(r,c)]
            value = matrix[r][c]
            path[(r,c)] = 1+max(dfs(r+1,c,value),
            dfs(r,c+1,value), dfs(r,c-1,value), dfs(r-1,c,value))
            return path[(r,c)]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j,float('-inf')))
        return res