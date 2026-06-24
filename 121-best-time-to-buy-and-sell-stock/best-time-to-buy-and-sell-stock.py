class Solution(object):
    def maxProfit(self, nums):
        buy=float('inf')
        max_profit=0
        for num in nums:
            purchase=num
            buy=min(buy,purchase)
            profit=num-buy
            max_profit=max(profit,max_profit)
        return max_profit
            
        
        