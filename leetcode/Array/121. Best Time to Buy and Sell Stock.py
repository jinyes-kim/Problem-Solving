class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -sys.maxsize
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
    
        return profit
