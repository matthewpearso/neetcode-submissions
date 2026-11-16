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
        
        for i in range(len(s)):
            cur = s[:i] + s[i+1:]
            if checkString(cur) == True:
                return True
        
        return False