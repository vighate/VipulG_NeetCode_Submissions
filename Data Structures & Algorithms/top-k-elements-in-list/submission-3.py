from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        d = Counter(nums)

        sorted_d = sorted(d.items(), key = lambda x:x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_d[i][0])
        
        return res