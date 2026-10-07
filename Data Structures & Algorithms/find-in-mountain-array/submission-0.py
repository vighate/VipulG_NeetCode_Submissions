class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        l = 0
        r = mountainArr.length()-1
        peak = 0

        while l < r:
            mid = (l+r)//2

            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid+1
            else:
                r = mid
        
        peak = l

        # left of peak
        l = 0
        r = peak

        while l <= r:
            mid = (l+r)//2

            if mountainArr.get(mid) == target:
                return mid

            elif mountainArr.get(mid) < target:
                l = mid+1
            else:
                r = mid-1

        # right of peak
        l = peak+1
        r = mountainArr.length()-1

        while l <= r:
            mid = (l+r)//2

            if mountainArr.get(mid) == target:
                return mid

            elif mountainArr.get(mid) > target:
                l = mid+1
            else:
                r = mid-1

        return -1


