class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l+r)//2

            days_needed = 1
            curr = 0

            for weight in weights:
                if curr+weight > mid:
                    days_needed+=1
                    curr = 0

                curr += weight

            if days_needed <= days:
                r = mid
            else:
                l = mid+1

        return l