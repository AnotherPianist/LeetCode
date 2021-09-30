class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target_sum, remainder = divmod(sum(nums), k)
        if remainder != 0:
            return False
        ks = [0] * k
        nums.sort(reverse=True)
        visited = set()
        
        def recursion(remaining_k, cur_sum, next_index):
            if remaining_k == 1:
                return True
            if cur_sum == target_sum:
                return recursion(remaining_k - 1, 0, 0)
            for i in range(next_index, len(nums)):
                if i not in visited and cur_sum + nums[i] <= target_sum:
                    visited.add(i)
                    if recursion(remaining_k, cur_sum + nums[i], i + 1):
                        return True
                    visited.remove(i)
            return False
        
        return recursion(k, 0, 0)