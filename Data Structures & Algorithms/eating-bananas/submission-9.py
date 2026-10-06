class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r)//2

            hours_to_eat = 0

            ## hours_to_eat = ceil(sum(piles)//mid)
            for pile in piles:
                hours_to_eat += (pile+mid-1)//mid

            if hours_to_eat <= h:
                r = mid
            else:
                l = mid+1

        return l