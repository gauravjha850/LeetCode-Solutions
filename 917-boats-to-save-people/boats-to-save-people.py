class Solution(object):
    def numRescueBoats(self, arr, limit):
        ans=0
        low=0
        arr.sort()
        high=len(arr)-1
        while low <= high :
            if arr[low]+arr[high] <= limit :
                ans=ans+1
                low=low+1
                high=high-1
            elif arr[low]+arr[high] > limit :
                high =high -1
                ans=ans+1
        return ans

        