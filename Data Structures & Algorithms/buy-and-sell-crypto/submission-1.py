class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0

        for num in prices:
            spend = num - mini
            profit = max(spend, profit)
            mini = min(num,mini)
        
        return profit
        