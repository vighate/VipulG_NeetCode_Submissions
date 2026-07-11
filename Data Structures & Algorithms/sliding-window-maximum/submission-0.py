class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        l = 0
        while l < len(nums)-k+1:
            max_value = max(nums[l:l+k])
            res.append(max_value)
            l += 1

        return res

        