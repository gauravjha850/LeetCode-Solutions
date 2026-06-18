class Solution(object):
    def runningSum(self, nums):
        sums=nums[0]
        for i in range (1,len(nums)):
            sums+=nums[i]
            nums[i]=sums
        return nums

        

        