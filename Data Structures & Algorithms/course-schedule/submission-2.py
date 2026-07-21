class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set()
        path = set()

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
            return True
        
        for i in range(numCourses):
            if dfs(i) ==False:
                return False
        
        return True