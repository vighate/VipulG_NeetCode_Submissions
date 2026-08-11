class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        d = {}

        for num in nums:
            if num in d:
                d[num]+=1
                return True
            else:
                d[num] = 1
        return False


        print("Hello")

        d = {}

        for num in nums:
            if num in d:
                d[num]+=1
                return True
            d[num] = 1
        
        return False