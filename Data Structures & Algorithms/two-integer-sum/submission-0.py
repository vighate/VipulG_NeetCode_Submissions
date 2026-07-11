class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i,j such that nums[i]+nums[j]==target and i != j


        d = {}

        res = []
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in d:
                return [d[diff],i]
            d[nums[i]] = i

        