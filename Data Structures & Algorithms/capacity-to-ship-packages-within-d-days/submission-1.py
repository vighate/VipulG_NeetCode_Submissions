class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l+r)//2

            day_needed = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > mid:
                    day_needed += 1
                    current_weight = 0
                current_weight += weight

            if day_needed <= days:
                r = mid-1
            else:
                l = mid+1

        return l

            