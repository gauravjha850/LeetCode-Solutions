class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count=0
        for num in costs:
            if coins>=num:
                count+=1
                coins-=num
            else:
                break
        return count
        
        