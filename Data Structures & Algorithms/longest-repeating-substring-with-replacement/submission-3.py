class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            choice = max(freq, key=freq.get)
            numReps = (r - l + 1) - freq[choice]

            if numReps > k:
                freq[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            

            r += 1
        
        return maxLen
            

            
        


        