class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = "".join([str(ord(c) - ord('a') + 1) for c in s])
        
        while k:
            nums = str(sum([int(c) for c in nums]))
            k -= 1
        
        return int(nums)