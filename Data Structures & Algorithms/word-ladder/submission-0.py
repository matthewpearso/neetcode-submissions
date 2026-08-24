class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def compare(word1, word2):
            i = 0
            diff = 0
            while i < len(word1) and i < len(word2):
                if diff > 1:
                    return False
                if word1[i] != word2[i]:
                    diff += 1
                i += 1
            return diff == 1
        
        allWords = wordList + [beginWord]
        
        adj = {}
        for word in allWords:
            adj[word] = []

        for i in allWords:
            for j in allWords:
                if i != j and compare(i, j):
                    adj[i].append(j)
                    adj[j].append(i)
        
        #####################################
        
        q = deque()
        visit = set()
        q.append(beginWord)
        visit.add(beginWord)
        count = 1
        while q:
            for i in range(len(q)):
                current = q.popleft()
                if current == endWord:
                        return count
                for nbr in adj[current]:
                    if nbr in visit:
                        continue
                    q.append(nbr)
                    visit.add(nbr)
            count += 1
        return 0

        
            
            








        