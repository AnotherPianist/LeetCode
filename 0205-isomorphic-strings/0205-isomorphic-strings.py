class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}
        
        for char_s, char_t in zip(s, t):
            if (char_s in map_s and map_s[char_s] != char_t) or (char_t in map_t and map_t[char_t] != char_s):
                return False
            map_s[char_s] = char_t
            map_t[char_t] = char_s

        return True