class Solution:
    def maxSubarraySumCircular(elf, nums: List[int]) -> int:
        
        currmax = nums[0]
        maxsum = nums[0]
        total = sum(nums)
        currmin = nums[0]
        minsum = nums[0]

        for num in nums[1:]:

            currmax = max(num, currmax+num)
            maxsum = max(maxsum, currmax)

            currmin = min(num, currmin+num)
            minsum = min(minsum, currmin)

        if maxsum < 0:
            return maxsum

        return max(maxsum, total-minsum)