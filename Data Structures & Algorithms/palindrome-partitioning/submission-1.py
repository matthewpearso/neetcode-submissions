class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def recurse(l, r, current):
            
            if l >= len(s):
                self.res.append(current.copy())
                return
            
            substr = s[l:r+1]
            
            if substr == substr[::-1]:
                current.append(substr)
                cut = recurse(r + 1, r + 1, current)
                current.pop()
            
            if r + 1 < len(s):
                skip = recurse(l, r + 1, current)

        
        recurse(0, 0, [])
        return self.res


        