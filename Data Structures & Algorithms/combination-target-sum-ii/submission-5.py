class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        res = []
        path = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0 or i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue

                if candidates[j] > remaining:
                    return 
                
                path.append(candidates[j])
                dfs(j+1, remaining-candidates[j])
                path.pop()
            
        dfs(0,target)
        return res

        nums = candidates

        nums = sorted(nums)

        res = []
        path = []

        def dfs(start, remaining):
            
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0 or start ==len(nums):
                return
            
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue

                if nums[i] > remaining:
                    return

                path.append(nums[i])
                dfs(i+1, remaining-nums[i])
                path.pop()
        
        dfs(0, target)
        return res