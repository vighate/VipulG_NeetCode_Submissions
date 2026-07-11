class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        memo = {}

        def dfs(left, right):

            if left>=right:
                return True

            if (left, right) in memo:
                return memo[(left, right)]

            if s[left] != s[right]:
                memo[(left, right)] = False
            else:
                memo[(left, right)] = dfs(left+1, right-1)

            return memo[(left, right)]

        res = []
        path = []

        def dfs2(start):

            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):

                if dfs(start, i):
                    path.append(s[start:i+1])
                    dfs2(i+1)
                    path.pop()

        dfs2(0)
        return res

        