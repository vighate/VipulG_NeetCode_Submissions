class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        windowsum = 0
        res = float('inf')

        for right in range(len(nums)):
            windowsum += nums[right]

            while windowsum >= target:
                res = min(res, right-left+1)
                windowsum -= nums[left]
                left += 1
        
        return 0 if res == float('inf') else res
