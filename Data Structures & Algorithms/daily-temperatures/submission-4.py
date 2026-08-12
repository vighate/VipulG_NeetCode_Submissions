class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        nums = temperatures
        res = [0]*len(nums)
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                prv = stack.pop()
                res[prv] = abs(i - prv)
            
            stack.append(i)
        
        return res
        
        
        
        
        nums = temperatures
        res = [0]*len(temperatures)

        stack = []

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                prv = stack.pop()
                res[prv] = i - prv
            
            stack.append(i)
        
        return res

        
        res = []
        l = 0

        nums = temperatures
        while l < len(nums):

            for i in range(l+1,len(nums)):
                if nums[i] > nums[l]:
                    res.append(i-l)
                    break
            else:
                res.append(0)
            
            l +=1
        
        return res