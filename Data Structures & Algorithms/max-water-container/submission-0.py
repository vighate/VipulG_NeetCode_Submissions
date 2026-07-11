class Solution:
    def maxArea(self, heights: List[int]) -> int:

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
        