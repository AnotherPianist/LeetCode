class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = highest_altitude = 0
        
        for net_gain in gain:
            altitude += net_gain
            highest_altitude = max(highest_altitude, altitude)
        
        return highest_altitude
