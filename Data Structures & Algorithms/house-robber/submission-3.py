class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            take = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            memo[i] = max(take,skip)
            return memo[i]

        return dfs(0)
        
        # if len(nums) == 0:
        #     return 0

        # if len(nums) == 1:
        #     return nums[0]

        # memo = {}

        # def dfs(i):

        #     if i >= len(nums):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     take = nums[i]+dfs(i+2)
        #     skip = dfs(i+1)

        #     memo[i] = max(take,skip)

        #     return memo[i]

        # return dfs(0)
            
