class Solution:
    def maxArea(self, heights: List[int]) -> int:

        nums = heights
        l = 0
        r = len(nums)-1
        max_val = float('-inf')
        while l < r:
            max_val = max(max_val, (r-l)*min(nums[l], nums[r]))

            if nums[l] < nums[r]:
                l +=1
            else:
                r-=1
            
        return max_val











        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            water = (r-l)*min(heights[l], heights[r])

            if res < water:
                res = water
            
            if heights[l] < heights[r]:
                l +=1
            else:
                r-= 1
        return res


        max_area = -10
        nums = heights
        l = 0
        r = len(nums)-1

        while l<r:
            curr = (r-l)*min(nums[l],nums[r])
            # 0,6,6
            # 1,
            if max_area < curr:
                max_area = curr

            if nums[l] < nums[r]:
                l +=1
            else:
                r -=1

        return max_area
        