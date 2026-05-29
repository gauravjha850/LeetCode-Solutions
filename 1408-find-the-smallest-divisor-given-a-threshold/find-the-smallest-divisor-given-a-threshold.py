class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        while low< high :
            mid=low+(high-low)//2
            total_sum=0
            for num in nums :
                total_sum+= (num+mid-1)//mid
            if total_sum <= threshold :
                high=mid
            else:
                low =mid+1
        return  low
        