class Solution(object):
    def sortArrayByParity(self, arr):
        low=0
        high=len(arr)-1
        while low < high:
            if arr[low]%2==0:
                low+=1
            elif arr[high]%2 !=0:
                high=high-1
            else:
                arr[low],arr[high]=arr[high],arr[low]
                low=low+1
                high=high-1
        return arr
        