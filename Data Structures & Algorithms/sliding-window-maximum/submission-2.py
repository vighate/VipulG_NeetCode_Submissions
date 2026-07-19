class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        i = 0
        while i <= len(nums)-k:
            maxsum = max(nums[i:i+k])
            res.append(maxsum)
            i+=1
        return res

        res = []
        l = 0

        while l < len(nums)-k+1:
            max_value = max(nums[l:l+k])
            res.append(max_value)
            l += 1

        return res

        