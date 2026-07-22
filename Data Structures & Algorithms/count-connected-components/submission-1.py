from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adj[node]:
                if n not in visited:
                    dfs(n)
        
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components +=1

        return components
























        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    dfs(n)
        comp = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                comp +=1
        return comp
