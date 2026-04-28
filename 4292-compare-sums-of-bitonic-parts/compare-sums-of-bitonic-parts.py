class Solution(object):
    def compareBitonicSums(self, nums):
        n=len(nums)
        peak_index=0
        for i in range (1,n-1):
            if nums[i-1]< nums[i] and nums[i] > nums[i+1] :
                peak_index=i
                break
        left_sum=sum(nums[:peak_index+1])
        right_sum=sum(nums[peak_index:])
        if left_sum > right_sum :
            return 0
        if right_sum>left_sum:
            return 1
        else:
            return -1

        

        