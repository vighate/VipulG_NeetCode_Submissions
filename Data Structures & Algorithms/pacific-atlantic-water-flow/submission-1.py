class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,visited,prevHeight):

            if (r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or heights[r][c]<prevHeight):
                return 
            visited.add((r,c))

            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            
        # pacific border
        for row in range(rows):
            dfs(row,0,pacific,heights[row][0])
            dfs(row,cols-1,atlantic,heights[row][cols-1])
            
        # atlantic border
        for col in range(cols):
            dfs(0,col,pacific,heights[0][col])
            dfs(rows-1,col,atlantic,heights[rows-1][col])
        
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res