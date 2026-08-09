class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        num = 0
        visited = []
        
        def dfs(r, c):
            if (r >= ROWS or r < 0 or
                c >= COLS or c < 0 or
                grid[r][c] == '0'):
                return 
            
            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    num += 1
                    dfs(r, c)
        
        return num




