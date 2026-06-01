class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        n=len(cost)
        i=n-1
        total=0

        while i>=0:
            total+=cost[i]
            if i-1 >=0:
                total+=cost[i-1]
            i=i-3

        return total
        


        
        