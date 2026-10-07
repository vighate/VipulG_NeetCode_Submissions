class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = (l+r)//2

            max_subarray = 1
            curr = 0

            for num in nums:
                if curr+num > mid:
                    max_subarray +=1
                    curr = 0
                curr += num

            if max_subarray <= k:
                r = mid
            else:
                l = mid+1

        return l