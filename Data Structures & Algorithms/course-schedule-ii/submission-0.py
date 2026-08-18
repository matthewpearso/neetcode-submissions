class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        cycle = set()
        valid = set()
        order = []

        def dfs(course):
            if course in cycle:
                return False
            if course in valid:
                return True
            
            cycle.add(course)
            
            for pre in graph[course]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(course)
            valid.add(course)
            order.append(course)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return order
            

            
    
            

        