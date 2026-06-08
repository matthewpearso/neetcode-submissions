class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        max_output = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            letter = max(freq, key=freq.get)
            reps_needed = (r - l + 1) - freq[letter]
            
            if reps_needed > k:
                freq[s[l]] -= 1
                l += 1

            max_output = max(r-l+1, max_output)
            

        return max_output
            

            
        


        