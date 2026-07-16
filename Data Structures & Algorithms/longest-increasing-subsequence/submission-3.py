class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dfs(start):

            if start == len(nums):
                return 0

            if start in memo:
                return memo[start]

            ans = 1

            for i in range(start, len(nums)):
                if nums[i] > nums[start]:
                    ans = max(ans, 1+dfs(i))

            memo[start] = ans
            return ans

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res









        # memo = {}

        # def dfs(i):

        #     if i == len(nums):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     ans = 1

        #     for j in range(i+1, len(nums)):
        #         if nums[j] > nums[i]:
        #             ans = max(ans, 1+dfs(j))

        #     memo[i] = ans
        #     return ans

        # res = 0
        # for i in range(len(nums)):
        #     res = max(res, dfs(i))
        # return res