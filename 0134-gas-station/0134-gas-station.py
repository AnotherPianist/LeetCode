class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = total_surplus = start = 0
        
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            
            if surplus < 0:
                surplus = 0
                start = i + 1
        
        return -1 if (total_surplus < 0) else start