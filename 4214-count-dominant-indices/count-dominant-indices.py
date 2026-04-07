class Solution(object):
    def dominantIndices(self, arr):
        total=sum(arr)
        right_sum=total
        n=len(arr)
        count=0
        for i in range(0,n-1):
            right_sum=right_sum-arr[i]
            remaining=(n-i-1)
            avg= (right_sum)/remaining
            
            if arr[i] > avg:

                count=count+1

                
        return count
            
            


        