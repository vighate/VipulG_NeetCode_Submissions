from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        it = []
        def dfs(node):
            while len(adj[node]) > 0:
                nei = adj[node].pop()
                dfs(nei)
            it.append(node)

        dfs("JFK")
        return it[::-1]

