class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in anagrams:
                value = anagrams[key]
                value.append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())