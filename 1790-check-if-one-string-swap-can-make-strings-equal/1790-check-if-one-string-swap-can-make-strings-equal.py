class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i1 = i2 = -1
        diff_count = 0
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                i2 = i1
                i1 = i
                diff_count += 1
                if diff_count > 2:
                    return False
                
        return diff_count == 0 or (diff_count != 1 and (s1[i1] == s2[i2] and s2[i1] == s1[i2]))