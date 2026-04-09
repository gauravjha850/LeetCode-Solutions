class Solution(object):
    def twoSum(self, arr, target):
        low=0
        high=len(arr)-1
        while low < high:
            if arr[low]+arr[high] == target:
                
                return [low+1,high+1]
            if arr[low] +arr[high] < target :
                low=low+1
            else:
                high=high-1
        return [-1,-1]
            
            
            

        