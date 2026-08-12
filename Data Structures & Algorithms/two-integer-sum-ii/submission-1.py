from collections import Counter
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(numbers)):

            diff = target - numbers[i]

            if diff in d:
                return [d[diff]+1,i+1]
            else:
                d[numbers[i]] = i


        
        # 2 sum problem
        nums = numbers
        d = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in d:
                return [d[diff]+1, i+1]
            d[nums[i]] = i

        