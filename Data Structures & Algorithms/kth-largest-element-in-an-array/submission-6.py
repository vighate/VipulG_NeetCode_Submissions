class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)

        return nums[len(nums)-k]

        def max_valfn(nums):

            max_val = float('-inf')

            for num in nums:
                max_val = max(max_val, num)
            
            return max_val
        
        res = []
        while k>=0:
            m = max_valfn(nums)
            nums.remove(m)
            if k==0:
                res.append(m)
            k-=1

        return res