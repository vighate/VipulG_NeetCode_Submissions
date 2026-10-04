import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {i: [] for i in range(n)}
        for s, d, c in flights:
            adj[s].append((d, c))

        minHeap = [(0,src,0)]

        dist = [[float('inf')]*(k+2) for _ in range(n)]

        dist[src][0] = 0

        while minHeap:
            cost, node, flights_used = heapq.heappop(minHeap)

            if node == dst:
                return cost
            
            if cost > dist[node][flights_used]:
                continue

            if flights_used == k+1:
                continue

            for d,c in adj[node]:
                new_cost = cost+c
                new_flights = flights_used + 1

                if new_cost < dist[d][new_flights]:
                    dist[d][new_flights] = new_cost
                    heapq.heappush(minHeap, (new_cost, d, new_flights))

        return -1

            





        adj = {i: [] for i in range(n)}

        for source, destination, cost in flights:
            adj[source].append((destination, cost))

        minHeap = [(0,src,k+1)]

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)
            if node == dst:
                return cost
            if stops == 0:
                continue
            for nei, price in adj[node]:
                heapq.heappush(minHeap, (cost+price, nei, stops-1))

        return -1
        
        # adj = defaultdict(list)
        # for s,d,c in flights:
        #     adj[s].append((d,c))

        # minHeap = [(0,src,k+1)]

        # while minHeap:

        #     cost, source, flights = heapq.heappop(minHeap)
        #     if source == dst:
        #         return cost
        #     if flights == 0:
        #         continue
        #     for nei, c in adj[source]:
        #         heapq.heappush(minHeap, (cost+c,nei,flights-1))

        # return -1

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