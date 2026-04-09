class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_cost=sum(cost)
        total_gas=sum(gas)
        if total_gas < total_cost:
            return -1
        start=0
        total=0

        
        for i in range(len(gas)):
            total=total+(gas[i]-cost[i])
            
            if total < 0:
                start=i+1
                total=0       
        return start
        
        