class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def canSplit(limit):

            currsum = 0
            count =1

            for num in nums:
                if currsum+num > limit:
                    count += 1
                    currsum = num
                else:
                    currsum += num

            return count <= k
        while l < r:

            mid = (l+r)//2

            if canSplit(mid):
                r = mid
            else:
                l = mid+1

        return l