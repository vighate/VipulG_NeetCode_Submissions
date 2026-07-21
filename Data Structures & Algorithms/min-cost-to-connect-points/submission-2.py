import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = [(0,0)]
        visited = set()
        ans = 0

        while len(visited) <len(points):
            
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            ans += cost

            x1, y1 = points[i]

            for j in range(len(points)):
                if j not in visited:
                    x2, y2 = points[j]

                    dist = abs(x1-x2) + abs(y2-y1)
                    heapq.heappush(minHeap, (dist,j))
        return ans