class Solution:
    def countSubstrings(self, s: str) -> int:
        
        memo = {}

        def dfs(left, right):

            if left >= right:
                return True

            if (left, right) in memo:
                return memo[(left, right)]

            if s[left] != s[right]:
                memo[(left, right)] = False
            else:
                memo[(left, right)] = dfs(left+1, right-1)

            return memo[(left, right)]

        count = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i,j):
                    count += 1

        return count