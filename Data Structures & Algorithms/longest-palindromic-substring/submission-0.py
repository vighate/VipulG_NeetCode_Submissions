class Solution:
    def longestPalindrome(self, s: str) -> str:
        
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

        max_len = 0
        start = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i,j):
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        start = i

        return s[start:start+max_len]