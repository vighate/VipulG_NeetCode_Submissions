
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []

        def dfs(start):

            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()

            # if start == len(nums):
            #     res.append(path[:])
            #     return 
            
            # dfs(start+1)
            # path.append(nums[start])
            # dfs(start+1)
            # path.pop()

        dfs(0)
        return res
        
        # res = [[]]

        # for num in nums:
        #     res += [curr + [num] for curr in res]

        # return res