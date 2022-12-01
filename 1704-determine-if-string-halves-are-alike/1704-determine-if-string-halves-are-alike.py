class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        counter1, counter2 = 0, 0
        
        for i, c in enumerate(s):
            if c in vowels:
                if i < len(s) // 2:
                    counter1 += 1
                else:
                    counter2 += 1
                
        return counter1 == counter2