class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        path = set()
        visited = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def dfs(course):
            # cycle detected
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)

            for pre in preMap[course]:
                if dfs(pre)==False:
                    return False
            path.remove(course)
            visited.add(course)
            return True 

        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True















        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()

        def dfs(course):

            if course in visited:
                return False

            if preMap[course] ==[]:
                return True

            visited.add(course)

            for pre in preMap[course]:
                if dfs(pre) ==False:
                    return False
            
            visited.remove(course)
            preMap[course] =[]
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        return True
