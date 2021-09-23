class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome.replace(palindrome[i], "a", 1)
        return "".join(list(palindrome)[:-1] + ["b"])