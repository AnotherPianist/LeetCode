from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        longest = 0
        
        for w in words:
            reversed_word = w[::-1]
            if reversed_word in seen and seen[reversed_word] > 0:
                seen[reversed_word] -= 1
                if seen[reversed_word] <= 0:
                    del seen[reversed_word]
                longest += 4
            else:
                seen[w] += 1
                
        for w in seen:
            if w[0] == w[1]:
                return longest + 2
        return longest