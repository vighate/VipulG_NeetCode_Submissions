class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1
        water = 0
        
        lh = height[l]
        rh = height[r]

        while l < r:
            if lh < rh:
                l +=1
                lh = max(lh, height[l])
                water += lh-height[l]
            
            else:
                r -= 1
                rh = max(rh, height[r])
                water += rh-height[r]
        
        
        
        return water



        
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

