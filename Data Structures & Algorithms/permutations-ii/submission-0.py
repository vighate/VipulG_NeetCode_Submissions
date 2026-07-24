from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num]-=1
                    dfs()
                    path.pop()
                    count[num] +=1
        dfs()
        return res