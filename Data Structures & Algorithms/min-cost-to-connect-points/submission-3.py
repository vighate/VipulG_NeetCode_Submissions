import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        minHeap = [(0,0)]
        visited = set()
        total_cost = 0
        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            total_cost +=cost
            visited.add(i)
            x1,y1 = points[i]
            for j in range(len(points)):
                x2,y2 = points[j]
                if j not in visited:
                    dist = abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(minHeap, (dist,j))

        return total_cost

















        minHeap = [(0,0)]
        ans = 0
        visited = set()
        while len(visited) < len(points):
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            ans += cost
            x1, y1 = points[i]
            for j in range(len(points)):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x2-x1) +abs(y2-y1)
                    heapq.heappush(minHeap, (dist, j))
        return ans


        


        # res = 0
        # minHeap = [(0,0)]
        # n = len(points)
        # visited = set()
        # while len(visited) < n:

        #     cost, i = heapq.heappop(minHeap)

        #     if i in visited:
        #         continue
            
        #     visited.add(i)

        #     res += cost
        #     x1, y1 = points[i]
        #     for j in range(n):
        #         if j not in visited:
        #             x2, y2 = points[j]
        #             dist = abs(x2-x1) +abs(y2-y1)
        #             heapq.heappush(minHeap, (dist,j))
        # return res  
