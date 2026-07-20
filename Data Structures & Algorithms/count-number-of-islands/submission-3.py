from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0":
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1":
                    islands+=1
                    dfs(r,c)
        return islands
























        # QUEUE solution

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands +=1
                    grid[r][c] =="0"
                    q = deque([(r,c)])

                    while q:

                        row, col = q.popleft()

                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = row+dr, col+dc
                            if ( 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1"):
                                grid[nr][nc]="0"
                                q.append((nr,nc))

        return islands

        # DFS solution
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r,c):

            if (r<0 or r>=rows
                or c<0 or c>=cols
                or grid[r][c]=="0"):
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] =="1":
                    islands += 1
                    dfs(i,j)
        return islands






        # if not grid:
        #     return 0
        
        # rows = len(grid)
        # cols = len(grid[0])
        # islands = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             islands += 1
        #             grid[r][c] = "0"
        #             q = deque([(r,c)])

        #             while q:
        #                 row,col = q.popleft()
        #                 for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        #                     nr = row+dr
        #                     nc = col+dc

        #                     if (0<=nc<cols and 0<=nr<rows and grid[nr][nc]=="1"):
        #                         grid[nr][nc]="0"
        #                         q.append((nr,nc))
        # return islands



        
        # rows = len(grid)
        # cols = len(grid[0])
        # islands = 0

        # def dfs(r,c):
        #     if (r < 0 or r>= rows or
        #         c < 0 or c>=cols or
        #         grid[r][c] == "0"):
        #         return
            
        #     grid[r][c] = "0"

        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c+1)
        #     dfs(r,c-1)

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "1":
        #             islands += 1
        #             dfs(i,j)

        # return islands 