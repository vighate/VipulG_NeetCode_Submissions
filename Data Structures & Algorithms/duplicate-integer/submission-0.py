class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print("Hello")

        d = {}

        for num in nums:
            if num in d:
                d[num]+=1
                return True
            d[num] = 1
        
        return False