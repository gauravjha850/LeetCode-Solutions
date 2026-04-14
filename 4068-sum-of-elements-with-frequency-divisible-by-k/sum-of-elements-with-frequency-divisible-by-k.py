class Solution(object):
    def sumDivisibleByK(self, nums, k):
        count={}
        total=0
        for num in nums :
            if num in count :
                count[num]=count[num]+1
            else:
                count[num]=1
        for num, value in count.items():
            if value %k ==0:
                total=total+ num*value
        return total
            
        
        