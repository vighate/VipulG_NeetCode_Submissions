class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        order = []
        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for pre in adj[course]:
                if dfs(pre) ==False:
                    return False
            path.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return order












        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visiting = set()
        visited = set()
        order = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return order

