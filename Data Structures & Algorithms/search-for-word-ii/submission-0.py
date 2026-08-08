class TrieNode():
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        # ---- Build Trie ----
        current = root
        for word in words:
            
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            
            current.wordEnd = True
            current = root
        # --------------------
        
        rows = len(board)
        cols = len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node, current):
            if (r >= rows or r < 0 or
                c >= cols or c < 0 or
                (r, c) in visited or 
                board[r][c] not in node.children):
                return

            node = node.children[board[r][c]]
            visited.add((r, c))
            current += board[r][c]
            
            if node.wordEnd:
                res.add(current)
            
            dfs(r + 1, c, node, current)
            dfs(r, c + 1, node, current)
            dfs(r - 1, c, node, current)
            dfs(r, c - 1, node, current)

            visited.remove((r, c))
            

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        
        return list(res)




