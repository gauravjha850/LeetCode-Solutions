class Solution(object):
    def maxProduct(self, nums):
        if not nums :
            return 0
        c_max=nums[0]
        c_min=nums[0]
        g_max=nums[0]
        for num in nums[1:] :
            if num <0:
                c_max,c_min=c_min,c_max
            c_max=max(num,num*c_max)
            c_min=min(num,num*c_min)
            g_max=max(c_max,g_max)
        return g_max
        