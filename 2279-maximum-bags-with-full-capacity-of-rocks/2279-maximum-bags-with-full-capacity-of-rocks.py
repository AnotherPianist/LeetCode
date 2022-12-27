class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        free_space = [cap - usage for usage, cap in zip(rocks, capacity)]
        free_space.sort()
        
        for i, remaining in enumerate(free_space):
            if remaining == 0:
                continue
            additionalRocks -= remaining
            if additionalRocks == 0:
                return i + 1
            elif additionalRocks < 0:
                return i
        return len(rocks)