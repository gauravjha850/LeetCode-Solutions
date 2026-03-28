class Solution(object):
    def minAbsoluteDifference(self, arr):
        last_index_1=-1
        last_index_2=-1
        ans=float('inf')
        for i in range (0,len(arr)):
            if arr[i]==0:
                continue
            elif arr[i]==1:
                last_index_1=i
                if last_index_2 !=-1:
                    diff=abs(last_index_2-last_index_1)
                    ans=min(ans,diff)

                
            else:
                last_index_2=i
                if last_index_1 != -1:
                    diff=abs(last_index_2-last_index_1)
                    ans=min(ans,diff)
            
            
        return ans if ans!=float('inf') else -1
            
        