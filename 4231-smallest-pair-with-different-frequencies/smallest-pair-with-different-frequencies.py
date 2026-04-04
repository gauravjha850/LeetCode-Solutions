class Solution(object):
    def minDistinctFreqPair(self, arr):
        freq={}
        m=len(arr)
        if m < 2:
            return [-1,-1]
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        if len(freq)==1:
            return [-1,-1]
        
        sorted_key=sorted(freq.keys())

        for i in range (len(sorted_key)):
            for j in range(i+1,len(sorted_key)):
                

                if freq[sorted_key[i]]!=freq[sorted_key[j]]:
                    return [sorted_key[i],sorted_key[j]]
        return [-1,-1]
        
        