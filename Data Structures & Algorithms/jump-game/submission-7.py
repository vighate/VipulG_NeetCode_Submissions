class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxreach = 0

        for i in range(len(nums)):

            if i > maxreach:
                return False

            maxreach = max(maxreach, nums[i]+i)

        return True