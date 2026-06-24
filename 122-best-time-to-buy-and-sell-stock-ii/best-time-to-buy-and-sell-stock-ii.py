class Solution(object):
    def maxProfit(self, nums):
        max_profit=0
        for i in range (1,len(nums)):
            if nums[i-1]<=nums[i]:
                max_profit+=nums[i]-nums[i-1]
        return max_profit
        
        