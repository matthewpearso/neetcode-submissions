class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_fruits = 0
        visited = set()
        q = deque()

        def addFresh(r, c):
            if (min(r, c) < 0 or r == ROWS or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visited):
                return
            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    num_fruits += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        if num_fruits == 0:
            return 0
        
        time = 0
        while q and len(visited) < num_fruits:
            for i in range(len(q)):
                current = q.popleft()
                r, c = current[0], current[1]
                grid[r][c] = 2
                addFresh(r + 1, c)
                addFresh(r - 1, c)
                addFresh(r, c + 1)
                addFresh(r, c - 1)
            time += 1
        
        return time if len(visited) == num_fruits else -1


