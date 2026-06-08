class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        max_len = 1
        substring = set()
        while r < len(s):
            substring.add(s[l])
            current_len = r - l + 1

            if s[l] == s[r] and r == l+1:
                l += 1
                r += 1
                continue
            
            if s[r] not in substring:
                substring.add(s[r])
                if current_len > max_len:
                    max_len = current_len
                r += 1
            else:
                substring.remove(s[l])
                l += 1

        return max_len