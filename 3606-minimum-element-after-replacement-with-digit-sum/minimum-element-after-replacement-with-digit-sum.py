class Solution(object):
    def minElement(self, nums):
        n=len(nums)
        for i in range (len(nums)):
            sums=0
            while nums[i]>0:
                remain=nums[i]%10
                sums=sums+remain
                nums[i]=nums[i]//10
            nums[i]=sums
        return min(nums)

        