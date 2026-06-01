class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        i=0
        count=0
        for j in range (n):
            if nums[j]==1:
                consi=j-i+1
                count=max(count,consi)
            elif nums[j]!=1:
                i=j+1
        
        return count
            

        
        
        