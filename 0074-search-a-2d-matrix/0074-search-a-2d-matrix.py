class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1

        while left <= right:
                mid = left + (right - left) // 2
                pivot_element = matrix[mid // m][mid % m]

                if target == pivot_element:
                    return True

                if target < pivot_element:
                    right = mid - 1
                else:
                    left = mid + 1

        return False