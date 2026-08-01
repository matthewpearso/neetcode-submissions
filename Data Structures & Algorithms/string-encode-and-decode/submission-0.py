class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        div = chr(255)
        cipher = 15
        for string in strs:
            for char in string:
                before = ord(char)
                if ord(char) + cipher < 255:
                    after = chr(ord(char) + cipher)
                else:
                    overflow = (ord(char) + cipher) - 254
                    after = chr((overflow - 1))
                encoded += after
            encoded += div
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        cipher = 15
        div = chr(255)

        def extract(char, cipher, div):
            diff = ord(char) - cipher
            if diff < 0:
                translate = 255 - diff
                res = chr(translate)
            else:
                res = chr(diff)
            return res
        
        current = ""
        i = 0
        while s:
            if i + 1 > len(s):
                break
            if s[i] == div:
                decoded.append(current)
                current = ""
            else:
                current += extract(s[i], cipher, div)
            i += 1
        
        return decoded




