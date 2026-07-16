class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        ans = float('inf')
        window = 0

        for right in range(len(nums)):

            window += nums[right]

            while window >= target:

                ans = min(ans, (right-left+1))
                window -= nums[left]
                left += 1
            
        return 0 if ans == float('inf') else ans