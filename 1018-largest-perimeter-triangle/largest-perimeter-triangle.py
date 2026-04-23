class Solution(object):
    def largestPerimeter(self, nums):
        
        nums.sort()
        n=len(nums)
        for i in range (n-1,1,-1):
            last=nums[i]
            second_last=nums[i-1]
            third_last=nums[i-2]
            if second_last + third_last > last :

                maxi=(second_last + third_last + last )
                return maxi
            
            
        return 0
        