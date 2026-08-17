import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        minHeap = [(0,0)]
        vis = set()
        cost = 0
        while minHeap:
            dist, i = heapq.heappop(minHeap)
            if i in vis:
                continue
            vis.add(i)
            cost += dist
            x1, y1 = points[i]
            for j in range(len(points)):
                if j not in vis:
                    x2, y2 = points[j]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(minHeap, (dist,j))
        return cost
