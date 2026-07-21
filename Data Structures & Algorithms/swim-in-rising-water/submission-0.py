import heapq
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        minHeap = [(grid[0][0],0,0)]
        visited = {(0,0)}

        while minHeap:

            time, x, y = heapq.heappop(minHeap)

            if x==len(grid)-1 and y == len(grid[0])-1:
                return time
            directions = [(1,0),(0,-1),(-1,0),(0,1)]

            for dr, dc in directions:
                nr, nc = x+dr, y+dc

                if (0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited):
                    visited.add((nr,nc))
                    heapq.heappush(minHeap, (max(time,grid[nr][nc]), nr, nc))

            
