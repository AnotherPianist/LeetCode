class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        chars = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = []
        
        def backtrack(i, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
            else:
                possible_chars = chars[digits[i]]
                
                for char in possible_chars:
                    path.append(char)
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        
        return combinations
