class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, (len(prices))):
                p = prices[j] - prices[i]
                if p >= profit:
                    profit = p
        return profit if profit >= 0 else 0