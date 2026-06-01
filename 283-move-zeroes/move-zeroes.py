class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        i=0
        for j in range (0,n):
            
            if  nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        while i <n:
            nums[i]=0
            i+=1

