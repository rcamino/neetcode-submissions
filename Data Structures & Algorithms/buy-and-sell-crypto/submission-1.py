class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        max_sell = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if price < min_buy:
                if min_buy < max_sell:
                    profit = max_sell - min_buy
                    max_profit = max(profit, max_profit)
                min_buy = price
                max_sell = price
            else:
                max_sell = max(price, max_sell)
        if min_buy < max_sell:
            profit = max_sell - min_buy
            max_profit = max(profit, max_profit)
        return max_profit
