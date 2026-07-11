class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        memo = {}
        def dfs(left, right):

            if left+1 == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            ans = 0
            for k in range(left+1, right):

                coins = (dfs(left, k) +
                        nums[left]*nums[k]*nums[right] + 
                        dfs(k, right))

                ans = max(ans, coins)

            memo[(left, right)] = ans
            return ans

        return dfs(0, len(nums)-1)
