class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 2 sum problem
        nums = numbers
        d = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in d:
                return [d[diff]+1, i+1]
            d[nums[i]] = i

        