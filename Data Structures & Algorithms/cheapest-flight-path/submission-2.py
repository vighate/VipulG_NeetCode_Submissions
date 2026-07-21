import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {i: [] for i in range(n)}

        for s, d, price in flights:
            adj[s].append((d, price))

        minHeap = [(0,src,k+1)]

        while minHeap:
            cost,node,stops = heapq.heappop(minHeap)
            if node ==dst:
                return cost
            if stops ==0:
                continue
            for nei, price in adj[node]:
                heapq.heappush(minHeap, (cost+price, nei, stops-1))
        return -1