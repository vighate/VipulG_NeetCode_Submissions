import heapq
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minHeap = [(grid[0][0],0,0)]
        visited = set()
        
        while minHeap:
            time, r,c  = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue

            visited.add((r,c))
            if r == len(grid)-1 and c == len(grid[0])-1:
                return time

            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited):
                    heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr,nc))
