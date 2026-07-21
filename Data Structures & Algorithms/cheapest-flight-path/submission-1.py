from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        minHeap = [(0, src, k+1)]
        ans = 0
        for s, d, cost in flights:
            adj[s].append((d,cost))
        while minHeap:
            cost, source, stops = heapq.heappop(minHeap)
            if source==dst:
                return cost
            if stops> 0:
                for node, price in adj[source]:
                    heapq.heappush(minHeap, (cost+price,node,stops-1))
        
        return -1
            