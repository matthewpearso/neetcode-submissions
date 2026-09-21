class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap = {}
        tmap = {}

        for c in t:
            if c not in tmap:
                tmap[c] = 0
            tmap[c] += 1

        need = len(tmap)
        have = 0

        res = ""
        l = 0
        r = 0
        smap[s[0]] = 1
        if s[0] in tmap and smap[s[0]] == tmap[s[0]]:
            have += 1

        while l < len(s):
            valid = (have == need)

            if valid:
                if not res or len(s[l:r+1]) < len(res):
                    res = s[l:r+1]

                # remove s[l] from window
                if s[l] in tmap and smap[s[l]] == tmap[s[l]]:
                    have -= 1
                smap[s[l]] -= 1
                l += 1
                continue

            if r < len(s) - 1:
                r += 1
                if s[r] not in smap:
                    smap[s[r]] = 1
                else:
                    smap[s[r]] += 1

                if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                    have += 1
            else:
                break

        return res