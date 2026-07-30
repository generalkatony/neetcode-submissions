class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y_len = len(matrix)
        x_len = len(matrix[0])

        left = 0
        right = (y_len * x_len) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // x_len][mid % x_len]

            if target == mid_val:
                return True
            elif target > mid_val:
                left = mid + 1
            else:
                right = mid - 1

        return False