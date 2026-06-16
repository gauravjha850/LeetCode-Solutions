class Solution(object):
    def maxProfit(self, prices):
        buy=float('inf')
        max_profit=0
        for num in prices:
            buy=min(num,buy)
            profit=num-buy
            max_profit=max(profit,max_profit)
        return max_profit
            

        