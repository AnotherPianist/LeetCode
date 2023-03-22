class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        connected_cities = {0, n}
        connected_length = 0
        
        while connected_length != len(connected_cities):
            connected_length = len(connected_cities)
            for a, b, d in roads:
                if a in connected_cities:
                    connected_cities.add(b)
                if b in connected_cities:
                    connected_cities.add(a)
            
        min_score = float("inf")
        for a, b, d in roads:
            if a in connected_cities or b in connected_cities:
                min_score = min(min_score, d)
                
        return min_score