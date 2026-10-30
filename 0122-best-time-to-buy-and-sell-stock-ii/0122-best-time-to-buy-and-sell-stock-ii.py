class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        for i in range(n-1):
            if prices[i]<prices[i+1]:
                pro = prices[i+1]-prices[i]
                profit = pro+profit
        return profit
