class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        
        while minHeap:
            t, i, j = heapq.heappop(minHeap)
            nbrs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            
            if i == ROWS - 1 and j == COLS - 1:
                return t

            for nbr in nbrs:
                i2, j2 = nbr
                
                if (i2 < 0 or j2 < 0 or
                    i2 >= ROWS or j2 >= COLS or
                    (i2, j2) in visited):
                    continue
                visited.add((i2, j2))
                heapq.heappush(minHeap, (max(t, grid[i2][j2]), i2, j2))

        

        
