class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        nums = height
        r = len(nums)-1

        lmax = nums[l]
        rmax = nums[r]

        water = 0

        while l < r:

            if lmax < rmax:
                l +=1
                lmax = max(lmax, nums[l])
                water += lmax-nums[l]

            else:
                r-=1
                rmax = max(rmax, nums[r])
                water += rmax-nums[r]

        return water

