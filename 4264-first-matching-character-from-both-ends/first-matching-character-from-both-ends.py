class Solution(object):
    def firstMatchingIndex(self, arr):
        low=0
        high=len(arr)-1

        while low <= high:
            if arr[low]==arr[high]:
                return low
            low=low+1
            high=high-1
        return -1
                