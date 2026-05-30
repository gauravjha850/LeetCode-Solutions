import math
class Solution(object):
    def sumFourDivisors(self, nums):
        total_sum=0
        
        for num in nums:
            seen=set()
            for i in range (1,int(math.sqrt(num))+1):
                if num %i ==0:
                    seen.add(i)
                    seen.add(num//i)
                if len(seen)>4:
                    break
            if len(seen)==4:
                total_sum+=sum(seen)
        return total_sum
                



        