class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for num in nums[1:]:

            tmp = currMax

            currMax = max(
                num,
                currMax+num,
                currMin+num
            )

            currMin = min(
                num,
                tmp+num,
                currMin+num
            )

            ans = max(ans, currMax)

        return ans

        