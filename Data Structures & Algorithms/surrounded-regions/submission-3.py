class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        region = set()
        edge = set()

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or 
                    c == 0 or c == COLS - 1) and board[r][c] == 'O': 
                    edge.add((r, c))
        
        def dfs(r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                board[r][c] == 'X' or (r, c) in region):
                return
            
            region.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for pair in edge:
            dfs(pair[0], pair[1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in region:
                    board[r][c] = 'X'
            
        


