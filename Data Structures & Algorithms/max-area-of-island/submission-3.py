class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = []
        self.size = 0

        def dfs(r, c):
            if (r >= ROWS or r < 0 or
                c >= COLS or c < 0 or
                grid[r][c] == 0):
                islands.append(self.size)
                return
            
            self.size += 1
            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    self.size = 0
        
        if not islands:
            return 0
        else:
            return max(islands)

