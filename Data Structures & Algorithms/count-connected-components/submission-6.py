from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:



        adj = defaultdict(list)
        for v, u in edges:
            adj[v].append(u)
            adj[u].append(v)

        vis = set()
        def dfs(node):
            #if node not in vis:
            vis.add(node)
            
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)

        ans = 0
        for node in range(n):
            if node not in vis:
                ans +=1
                dfs(node)

        return ans








        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        path = set()

        def dfs(node):
            if node in path:
                return
            path.add(node)
            for nei in adj[node]:
                if nei not in path:
                    dfs(nei)
        graphs = 0
        for i in range(n):
            if i not in path:
                dfs(i)
                graphs += 1
        return graphs