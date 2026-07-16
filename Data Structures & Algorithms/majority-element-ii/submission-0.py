class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        d = {}

        for num in nums:
            d[num] = d.get(num,0)+1

        print(d)

        target = len(nums)/3
        print(target)
        res = []
        for num, freq in d.items():
            if freq > target:
                res.append(num)

        print(res)

        return res