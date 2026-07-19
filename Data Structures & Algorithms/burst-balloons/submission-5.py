class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        if not nums:
            return 0

        memo = {}
        nums = [1] + nums + [1]

        def dfs(l,r):
            if l+1 == r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            ans = 0
            for i in range(l+1,r):
                coins = (dfs(l,i) + nums[l]*nums[i]*nums[r] + dfs(i,r))
                ans = max(ans, coins)

            memo[(l,r)] = ans
            return ans
        
        return dfs(0, len(nums)-1)
        return ans




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
