class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        
        f = [[] for i in range(len(nums)+1)]
        for num, count in d.items():
            f[count].append(num)
        res = []
        for i in range(len(f)-1,0,-1):
            for num in f[i]:
                print(num)
                res.append(num)

                if len(res)==k:
                    return res
