class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
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