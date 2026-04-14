class Solution(object):
    def countSubarrays(self, nums):
        count=0
        n=len(nums)
        for i in range (1,n-1):
            if (nums[i-1]+nums[i+1])*2 == nums[i] :
                count=count+1
        return count
            


            
            



        
        