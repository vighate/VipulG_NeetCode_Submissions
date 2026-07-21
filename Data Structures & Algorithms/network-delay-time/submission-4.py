import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i: [] for i in range(1,n+1)}
        for u,v,w in times:
            adj[u].append((v,w))
        ans = 0

        minHeap = [(0,k)]
        visited = set()
        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            ans = time

            for nei, t in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time+t,nei))
        
        return ans if len(visited) ==n else -1
