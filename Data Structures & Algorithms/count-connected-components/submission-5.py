from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        


        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        vis = set()
        def dfs(node):
            vis.add(node)
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)
                
        ans = 0
        for i in range(n):
            if i not in vis:
                ans += 1
                dfs(i)

        return ans



        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        components = 0
        vis = set()
        def dfs(node):
            vis.add(node)
            for nei in graph[node]:
                if nei not in vis:
                    dfs(nei)
        
        for i in range(n):
            if i not in vis:
                components+=1
                dfs(i)
        return components




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



