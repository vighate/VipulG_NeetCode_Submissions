
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxreach = 0
        for i in range(len(nums)):

            if i > maxreach:
                return False

            maxreach = max(maxreach, nums[i]+i)

        return True





        # maxReach = 0

        # for i in range(len(nums)):

        #     if i > maxReach:
        #         return False

        #     maxReach = max(maxReach, nums[i]+i)

        # return True

        # # memo = {}

        # # def dfs(i):

        # #     if i>=len(nums)-1:
        # #         return True

        # #     if i in memo:
        #         return memo[i]

        #     for jump in range(1, nums[i]+1):
        #         if dfs(i+jump):
        #             memo[i] = True
        #             return True

        #     memo[i] = False
        #     return False

        # return dfs(0)