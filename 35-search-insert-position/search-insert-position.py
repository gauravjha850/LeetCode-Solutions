class Solution(object):
    def searchInsert(self, arr, target):
        low=0
        high=len(arr)
        while low < high :
            mid= low +(high-low)//2
             
            if arr[mid]< target:
                low=mid+1
            else:
                high =mid
        return low
        
        