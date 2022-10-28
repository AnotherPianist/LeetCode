from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def non_zero_cells(matrix):
            coords = []
            
            for i, row in enumerate(matrix):
                for j, val in enumerate(row):
                    if val == 1:
                        coords.append((i, j))
            
            return coords
        
        img1_ones, img2_ones = non_zero_cells(img1), non_zero_cells(img2)
        
        max_overlaps = 0
        vector_counts = Counter()
        
        for i1, j1 in img1_ones:
            for i2, j2 in img2_ones:
                displacement_vector = (i2 - i1, j2 - j1)
                vector_counts[displacement_vector] += 1
                
        most_common = vector_counts.most_common(1)
        max_count = most_common[0][1] if most_common else 0
        
        return max_count