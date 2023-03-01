#################################################################
        #                   Merge Sort                  #

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:

#         temp_arr = [0] * len(nums)
        
#         def merge(left, mid, right):
#             for i in range(mid - left + 1):
#                 temp_arr[left + i] = nums[left + i]
#             for i in range(right - mid):
#                 temp_arr[mid + 1 + i] = nums[mid + 1 + i]
                
#             i, j, k = 0, 0, left
            
#             while i < mid - left + 1 and j < right - mid:
#                 if temp_arr[left + i] <= temp_arr[mid + 1 + j]:
#                     nums[k] = temp_arr[left + i]
#                     i += 1
#                 else:
#                     nums[k] = temp_arr[mid + 1 + j]
#                     j += 1
#                 k += 1
            
#             while i < mid - left + 1:
#                 nums[k] = temp_arr[left + i]
#                 i += 1
#                 k += 1
#             while j < right - mid:
#                 nums[k] = temp_arr[mid + 1 + j]
#                 j += 1
#                 k += 1
        
#         def merge_sort(left, right):
#             if left >= right:
#                 return
            
#             mid = left + (right - left) // 2
            
#             merge_sort(left, mid)
#             merge_sort(mid + 1, right)
#             merge(left, mid, right)
        
#         merge_sort(0, len(nums) - 1)
        
#         return nums
    


#################################################################
        #                   Heap Sort                  #
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(n, i):  # top-down
            largest = i
            left, right = 2 * i + 1, 2 * i + 2
            
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)
        
        def heap_sort():
            for i in range(len(nums) // 2 - 1, -1, -1):
                heapify(len(nums), i)
            
            for i in range(len(nums) - 1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)
        
        heap_sort()
        return nums