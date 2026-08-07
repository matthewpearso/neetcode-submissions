class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        current.wordEnd = True
        
        return

    def search(self, word: str) -> bool:
        
        def dfs(i, current):
            if i == len(word):
                if current.wordEnd:
                    return True
                return False
            
            if not current.children or (word[i] != "." and word[i] not in current.children):
                return False
            
            if word[i] in current.children:
                current = current.children[word[i]]
                return dfs(i + 1, current)
            
            if word[i] == ".":
                for child in current.children:
                    if dfs(i + 1, current.children[child]):
                        return True
            
            return False
            
        return dfs(0, self.root)
        
