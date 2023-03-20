class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i, val in enumerate(flowerbed):
            if not val and (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
                flowerbed[i] = 1
                count += 1
                
                if count >= n:
                    return True
        
        return count >= n