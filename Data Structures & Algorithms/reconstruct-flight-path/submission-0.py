class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        it = []
        def dfs(source):
            while len(adj[source]) > 0:
                nxt = adj[source].pop()
                dfs(nxt)
            it.append(source)
        dfs("JFK")
        return it[::-1]