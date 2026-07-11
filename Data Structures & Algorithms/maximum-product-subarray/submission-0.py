class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for num in nums[1:]:

            tmp = currMax

            currMax = max(
                num,
                num*currMax,
                num*currMin
            )

            currMin = min(
                num,
                num*tmp,
                num*currMin
            )

            ans = max(ans, currMax)

        return ans

        
        
        