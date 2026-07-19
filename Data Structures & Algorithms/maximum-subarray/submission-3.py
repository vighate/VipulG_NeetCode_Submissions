class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        maxsum = nums[0]
        minsum = nums[0]

        for num in nums[1:]:
            tmp = maxsum
            maxsum = max(maxsum+num, minsum+num, num)
            minsum = min(minsum+num, tmp+num, num)
            ans = max(maxsum, ans)
        return ans




        ans = nums[0]
        currmax = nums[0]
        currmin = nums[0]

        for num in nums[1:]:

            tmp = currmax

            currmax = max(num, currmax+num, currmin+num)

            currmin = min(num, tmp+num, currmin+num)

            ans = max(ans, currmax)

        return ans
        
        # ans = nums[0]
        # currMax = nums[0]
        # currMin = nums[0]

        # for num in nums[1:]:

        #     tmp = currMax

        #     currMax = max(
        #         num,
        #         currMax+num,
        #         currMin+num
        #     )

        #     currMin = min(
        #         num,
        #         tmp+num,
        #         currMin+num
        #     )

        #     ans = max(ans, currMax)

        # return ans

        