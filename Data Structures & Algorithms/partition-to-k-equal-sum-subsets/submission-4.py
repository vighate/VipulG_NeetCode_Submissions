class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        if total%k != 0:
            return False
        
        path = [0]*k
        nums = sorted(nums, reverse=True)
        target = total//k
        def dfs(start):
            if start==len(nums):
                return True
            num = nums[start]
            for i in range(k):
                if path[i]+num <=target:
                    path[i]+=num

                    if dfs(start+1)==True:
                        return True
                    
                    path[i]-=num

                if path[i]==0:
                    break
            return False
        return dfs(0)