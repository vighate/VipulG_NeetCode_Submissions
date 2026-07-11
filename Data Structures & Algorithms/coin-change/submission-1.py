class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(remaining):

            if remaining==0:
                return 0

            if remaining in memo:
                return memo[remaining]

            if remaining<0:
                return float('inf')

            ans = float('inf')
            for coin in coins:
                ans = min(ans, 1+dfs(remaining-coin))

            memo[remaining]=ans

            return memo[remaining]

        ans = dfs(amount)
        return -1 if ans == float('inf') else ans