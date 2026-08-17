class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        path = set()
        vis = set()
        order = []

        def dfs(course):
            if course in path:
                return False
            if course in vis:
                return True
            path.add(course)
            for pre in adj[course]:
                if dfs(pre) == False:
                    return False
            path.remove(course)
            vis.add(course)
            order.append(course)
            

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return order 



        
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        path = set()
        visi = set()
        order = []
        def dfs(course):
            if course in path:
                return False
            if course in visi:
                return True
            path.add(course)
            for pre in adj[course]:
                if dfs(pre) == False:
                    return False
            path.remove(course)
            visi.add(course)
            order.append(course)
            return True
            
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return order



        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        visited = set()
        path = set()
        order = []

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for pre in adj[course]:
                if dfs(pre)==False:
                    return False
            
            path.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if dfs(course)==False:
                return []
        return order

