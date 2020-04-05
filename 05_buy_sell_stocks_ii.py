class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        max_profit = 0
        
        previous_day_price = prices[0]
        
        for current_day_price in prices[1:]:
            if current_day_price > previous_day_price:
                max_profit += current_day_price - previous_day_price
            previous_day_price = current_day_price
        return max_profit
