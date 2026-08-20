class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return

            visit.add(node)

            for nbr in adj[node]:
                if nbr == prev:
                    continue
                dfs(nbr, node)
        
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i, -1)

        return count
        

        

        

            

        



                
        

            