class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows*cols - 1

        while l<=r:

            mid = (l+r)//2

            row = mid//cols
            col = mid%cols

            value = matrix[row][col]

            if value == target:
                return True
            
            if value > target:
                r-=1
            else:
                l+=1

        return False