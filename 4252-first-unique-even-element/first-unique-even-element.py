class Solution(object):
    def firstUniqueEven(self, arr):
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        for x in arr:
            if x%2==0 and freq[x]==1:
                return x
        return -1
        

        
        