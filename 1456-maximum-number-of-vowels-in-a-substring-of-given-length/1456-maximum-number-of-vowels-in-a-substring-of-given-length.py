class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        max_count = 0
        
        for i in range(k):
            max_count += s[i] in vowels
        
        count = max_count
        
        for i in range(k, len(s)):
            count += s[i] in vowels
            count -= s[i - k] in vowels
            max_count = max(max_count, count)
        
        return max_count