class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        
        def dfs(node, parent):
            
            if node in visited:
                return False
            
            visited.add(node)
            
            for nbr in adj[node]:
                if nbr != parent:
                    if dfs(nbr, node) == False:
                        return False
        
            return True
        
        return dfs(0, -1) and len(visited) == n

