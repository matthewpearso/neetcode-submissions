class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = []
    
        while low <= high:
            mid = (low + high) // 2
            first = matrix[mid][0]
            last = matrix[mid][-1]

            if target < first:
                high = mid - 1
            elif target > last:
                low = mid + 1
            else:
                row = matrix[mid]
                break
        
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif target > row[mid]:
                low = mid + 1
            elif target < row[mid]:
                high = mid - 1
        
        return False

        