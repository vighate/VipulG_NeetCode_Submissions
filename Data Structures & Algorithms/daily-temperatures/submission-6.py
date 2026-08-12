class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []
        nums = temperatures

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                prv = stack.pop()
                res[prv] = abs(i-prv)
            stack.append(i)

        return res

        res = []
        nums = temperatures

        for i in range(len(nums)):
            val1 = nums[i]

            for j in range(i+1, len(nums)):

                if val1 < nums[j]:
                    res.append(j-i)
                    break
            else:
                res.append(0)

        return res