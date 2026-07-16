class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curr_sum = 0
        window = {0:1}
        res = 0

        for num in nums:
            curr_sum += num

            difference = curr_sum-k

            if difference in window:
                res += window[difference]

            window[curr_sum] = window.get(curr_sum, 0)+1

        return res
