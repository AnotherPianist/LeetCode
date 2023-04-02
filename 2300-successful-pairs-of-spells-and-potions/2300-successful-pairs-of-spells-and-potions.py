from math import ceil
from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        
        for spell in spells:
            min_val = ceil(success / spell)
            
            if min_val > potions[-1]:
                pairs.append(0)
            else:
                i = bisect_left(potions, min_val)
                pairs.append(len(potions) - i)
        
        return pairs