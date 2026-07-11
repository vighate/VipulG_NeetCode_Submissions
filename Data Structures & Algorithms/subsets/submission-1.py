
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []

        def dfs(start):

            if start == len(nums):
                res.append(path[:])
                return 
            
            dfs(start+1)
            path.append(nums[start])
            dfs(start+1)
            path.pop()

        dfs(0)
        return res
        
        # res = [[]]

        # for num in nums:
        #     res += [curr + [num] for curr in res]

        # return res