class Solution(object):
    def maxFrequency(self, arr, k):
        arr.sort()
        low=0
        max_len=0
        total=0
        for high in range(len(arr)):
            total= total + arr[high]
            
            while (arr[high]*(high - low +1)-total) > k:

                total = total-arr[low]
                low=low + 1
            max_len=max(high - low +1,max_len)
        return max_len

        
        