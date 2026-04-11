class Solution(object):
    def removeDuplicates(self, arr):
        n=len(arr)
        i=0
        for j in range (1,len(arr)):
            if arr[i]==arr[j]:
                continue
            elif arr[i]!=arr[j]:
                i=i+1
                arr[i]=arr[j]
        return i+1
        
        