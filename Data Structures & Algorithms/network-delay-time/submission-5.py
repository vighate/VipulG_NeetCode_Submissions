from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i: [] for i in range(1,n+1)}
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        
        visited = set()
        minHeap = [(0,k)]

        min_time = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            min_time = time

            for v,w in adj[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (time+w,v))

        return min_time if len(visited)==n else -1


































        adj = defaultdict(list)
        t = 0
        visited = set()
        minHeap = [(0,k)]        

        for u,v,w in times:
            adj[u].append((v,w))

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = time

            for v,w in adj[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (time+w,v))

        return t if len(visited)==n else -1

