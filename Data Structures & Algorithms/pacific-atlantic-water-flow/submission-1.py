class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = []
        atlantic = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.append((r, c))
                if (r == ROWS - 1 or 
                    c == COLS - 1):
                    atlantic.append((r, c))
        
        def dfs(r, c, prev, ocean):
            if (r >= ROWS or r < 0 or c >= COLS or c < 0 or
                heights[r][c] < prev or (r, c) in visited):
                return
            
            ocean.add((r, c))
            visited.add((r, c))
            prev = heights[r][c]
            
            dfs(r + 1, c, prev, ocean)
            dfs(r - 1, c, prev, ocean)
            dfs(r, c + 1, prev, ocean)
            dfs(r, c - 1, prev, ocean)
        
        p_set = set()
        a_set = set()

        visited = set()
        for cell in pacific:
            r, c = cell
            dfs(r, c, -1, p_set)
        
        visited = set()
        for cell in atlantic:
            r, c = cell
            dfs(r, c, -1, a_set)

        return list(p_set & a_set)



        