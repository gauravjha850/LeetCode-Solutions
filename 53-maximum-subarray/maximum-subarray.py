class Solution(object):
    def maxSubArray(self,arr):
        max_sum=arr[0]
        current_sum=arr[0]
        for i in range(1,len(arr)):
            
            
            current_sum=max(current_sum+arr[i],arr[i])
            max_sum=max(current_sum,max_sum)
            
        return max_sum
            
        