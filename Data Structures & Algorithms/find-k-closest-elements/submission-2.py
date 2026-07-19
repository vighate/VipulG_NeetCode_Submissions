class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l = 0
        r = len(arr)-k
        while l<r:
            mid = (l+r)//2
            if x - arr[mid] > arr[mid+k] - x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]
        




        left = 0
        right = len(arr)-k

        while left < right:

            mid = (left+right)//2

            if x - arr[mid] > arr[mid+k] - x:
                left = mid+1
            else:
                right = mid

        return arr[left:left+k]