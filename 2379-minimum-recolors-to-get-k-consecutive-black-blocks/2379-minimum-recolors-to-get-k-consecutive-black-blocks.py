class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        
        for i in range(k):
            if blocks[i] == "W":
                white += 1
        
        min_recolors = white
        
        for i in range(k, len(blocks)):
            white -= blocks[i - k] == "W"
            if blocks[i] == "W":
                white += 1
            min_recolors = min(min_recolors, white)
            
        return min_recolors