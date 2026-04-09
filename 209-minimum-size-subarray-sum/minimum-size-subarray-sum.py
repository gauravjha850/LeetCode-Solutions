class Solution(object):
    def minSubArrayLen(self, target, arr):
        left=0
        current_sum=0
        min_length=float('inf')
        for right in range (len(arr)):
            current_sum= current_sum +arr[right]
            while current_sum >= target :

                min_length=min(min_length,right-left+1)
                current_sum= current_sum-arr[left]
                left=left+1
        return min_length  if min_length != float('inf') else 0
