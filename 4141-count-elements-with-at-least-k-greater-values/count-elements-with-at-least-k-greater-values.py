class Solution(object):
    def countElements(self, nums, k):
        nums.sort()
        n=len(nums)
        value=0
        right=0
        for i in range (n):
            while right < n and nums[right] <= nums[i] :
                right=right+1
            count = n-right

            if count >= k:
                value=value+1
            else:
                break
        return value
            
            




        