class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = sum(nums)

        ans = nums[0]
        currmax = nums[0]
        currmin = nums[0]
        
        for num in nums[1:]:

            tmp = currmax

            currmax = max(num, currmax+num, currmin+num)
            currmin = min(num, tmp+num, currmin+num)
            ans = max(ans, currmax)

        return ans