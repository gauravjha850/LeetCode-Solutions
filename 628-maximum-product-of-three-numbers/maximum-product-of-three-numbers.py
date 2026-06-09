import heapq
class Solution(object):
    def maximumProduct(self, nums):
        three=heapq.nlargest(3,nums)
        two=heapq.nsmallest(2,nums)
        option1=three[0]*three[1]*three[2]
        option2=two[0]*two[1]*three[0]
        return max(option1,option2)
        
        