class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):

            if i>=len(nums)-1:
                return 0

            if i in memo:
                return memo[i]

            ans = float('inf')

            for jump in range(1, nums[i]+1):
                ans = min(ans, 1+dfs(i+jump))

            memo[i] = ans
            return ans
        return dfs(0)
