class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
    
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            take = nums[i]+dfs(i+2) 
            skip = dfs(i+1)
            memo[i] = max(take,skip)
            return memo[i]

        return max(dfs(0), dfs(1))