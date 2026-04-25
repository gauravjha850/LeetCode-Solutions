class Solution(object):
    def canPlaceFlowers(self, arr, n):
        length=len(arr)
        count=0
        for i in range (length):
            if arr[i]==0 :
                if i==0:
                    if length ==1 or arr[i+1]==0:
                        arr[i]=1
                        count+=1
                elif i==length-1:
                    if arr[i-1]==0:
                        arr[i-1]=1
                        count+=1
                else:
                    if arr[i-1]==0 and arr[i+1]==0:
                        arr[i]=1
                        count+=1
        return count>=n
                        