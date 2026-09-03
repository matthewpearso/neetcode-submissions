class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        string = ""
        stringLen = 0

        def isPalindrome(string):
            if string == string[::-1]:
                return True
            return False

        for i in range(len(s)):
            l, r = i, i
            current = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > stringLen:
                    string = s[l:r+1]
                    stringLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > stringLen:
                    string = s[l:r+1]
                    stringLen = r - l + 1
                l -= 1
                r += 1
            
        return string
