class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        used = [False for i in range(len(nums))]

        def dfs():

            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):

                if used[i]==True:
                    continue
                path.append(nums[i])
                used[i] = True

                dfs()
                path.pop()
                used[i] = False

        dfs()
        return res
            
        # res = []
        # path = []

        # used = [False for i in range(len(nums))]
        
        # def dfs():
        #     if len(path)==len(nums):
        #         res.append(path[:])
        #         return
            
        #     for i in range(len(nums)):
        #         if used[i]==True:
        #             continue
                
        #         used[i] = True
        #         path.append(nums[i])

        #         dfs()
        #         path.pop()
        #         used[i] = False

        # dfs()
        # return res
