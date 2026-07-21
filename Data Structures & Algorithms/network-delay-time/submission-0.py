from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

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

