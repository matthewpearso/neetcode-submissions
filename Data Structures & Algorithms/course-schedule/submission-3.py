class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if not graph[course]:
                return True
            
            visited.add(course)
        
            for pre in graph[course]:
                if dfs(pre) == False:
                    return False

            visited.remove(course)
            graph[course] = []
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True

            
