class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.length = len(board)
        self.width = len(board[0])

        def recurse(i, j, index, current, visited):
            if current == word:
                return True
            
            char = board[i][j]
            target = word[index]

            if char != target or (i, j) in visited:
                return False
            
            visited.add((i, j))
            
            if i > 0:
                top = recurse(i - 1, j, index + 1, current + char, visited)
            else:
                top = False
            
            if i + 1 < self.length:
                bottom = recurse(i + 1, j, index + 1, current + char, visited)
            else:
                bottom = False
            
            if j > 0:
                left = recurse(i, j - 1, index + 1, current + char, visited)
            else: 
                left = False

            if j + 1 < self.width:
                right = recurse(i, j + 1, index + 1, current + char, visited)
            else:
                right = False
            visited.remove((i, j))
            
            return top or bottom or left or right
        
        for i in range(self.length):
            for j in range(self.width):
                if board[i][j] == word[0]:
                    if board[i][j] == word:
                        return True
                    
                    current = ""
                    visited = set()
                    if recurse(i, j, 0, current, visited) == True:
                        return True
        
        return False
        
        
            
            
            