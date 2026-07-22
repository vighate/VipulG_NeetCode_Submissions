from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        components = 0
        def dfs(node):

            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                components +=1
                dfs(i)
        
        return components



