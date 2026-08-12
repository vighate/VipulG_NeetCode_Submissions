class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        min_val = float('inf')
        for price in prices:
            min_val = min(price, min_val)
            profit = max(profit, abs(price-min_val))
        
        return profit