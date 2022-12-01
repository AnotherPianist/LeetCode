class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        half = len(s) // 2
        counter = 0
        
        for i in range(half):
            if s[i] in vowels:
                counter += 1
            if s[half + i] in vowels:
                counter -= 1
                
        print(counter)
        return counter == 0