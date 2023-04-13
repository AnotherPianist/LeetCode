from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote, magazine = Counter(ransomNote), Counter(magazine)
        
        for char, count in ransomNote.items():
            if magazine[char] < count:
                return False
        
        return True