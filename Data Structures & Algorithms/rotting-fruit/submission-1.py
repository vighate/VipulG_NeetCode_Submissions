from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==2:
                    q.append((r,c))
                elif grid[r][c] ==1:
                    fresh +=1

        minutes = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                        grid[nr][nc] = 2
                        fresh-=1
                        q.append((nr,nc))

            minutes +=1
        return minutes if fresh ==0 else -1
             