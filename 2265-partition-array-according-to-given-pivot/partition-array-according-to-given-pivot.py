class Solution(object):
    def pivotArray(self, nums, pivot):
        n=len(nums)
        left=0
        right=n-1
        ans=[pivot]*n
        for i in range (n) :
            if nums[i] < pivot:
                ans[left]=nums[i]
                left+=1
            j=n-1-i
            if nums[j]>pivot:
                ans[right]=nums[j]
                right-=1
        return ans

            
        
        