class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        
        for num in nums:
            tmp = num
            while tmp % 2 == 0:
                tmp //= 2
            heap.append((tmp, max(num, tmp * 2)))
        
        max_val = max(i for i, _ in heap)
        heapify(heap)
        res = float("inf")
        
        while len(heap) == len(nums):
            num, limit = heappop(heap)
            res = min(res, max_val - num)
            if num < limit:
                heappush(heap, (num * 2, limit  ))
                max_val = max(max_val, num * 2)
        
        return res