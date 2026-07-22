class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        


    
        rows = len(matrix)
        cols = len(matrix[0])

        path = {}

        def dfs(r,c,length):

            if (r<0 or r>=rows or 
                c<0 or c>=cols or matrix[r][c] <= length):
                return 0

            if (r,c) in path:
                return path[(r,c)]

            val = matrix[r][c]
            path[(r,c)] = 1+max(
                dfs(r+1,c,val),
                dfs(r,c+1,val),
                dfs(r-1,c,val),
                dfs(r,c-1,val)
            )
            return path[(r,c)]

        res = 0
        for row in range(rows):
            for c in range(cols):
                res = max(res, dfs(row,c,float('-inf')))
        return res