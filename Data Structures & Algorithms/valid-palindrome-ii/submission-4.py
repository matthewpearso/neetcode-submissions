class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkString(s):
            length = len(s)

            if length % 2 == 0:
                l = length // 2 - 1
                r = l + 1
            else:
                l = r = length // 2
            
            while l >= 0 and r <= length:
                if s[l] != s[r]:
                    return False
                l -= 1
                r += 1
            
            return True
        
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                removeLeft = checkString(s[:l] + s[l+1:])
                removeRight = checkString(s[:r] + s[r+1:])
                return (removeLeft or removeRight)
            l += 1
            r -= 1
        
        return True
        