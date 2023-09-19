class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        node = nums[-1]

        for _ in range(n + 1):
            node = nums[node - 1]
        
        cycle_length = 1
        slow, fast = node, nums[node - 1]

        while slow != fast:
            slow = nums[slow - 1]
            fast = nums[nums[fast - 1] - 1]
            cycle_length += 1
        
        slow = fast = nums[-1]

        for _ in range(cycle_length):
            fast = nums[fast - 1]
        
        while slow != fast:
            slow = nums[slow - 1]
            fast = nums[fast - 1]
        
        return slow
