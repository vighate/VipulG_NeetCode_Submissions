class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,visited,pre):

            if (r<0 or r>=rows or c<0 or c>=cols or heights[r][c] < pre or (r,c) in visited):
                return
            
            visited.add((r,c))

            val = heights[r][c]
            dfs(r+1,c,visited,val)
            dfs(r-1,c,visited,val)
            dfs(r,c+1,visited,val)
            dfs(r,c-1,visited,val)

        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])
        
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        
        return list(pacific & atlantic)

            
