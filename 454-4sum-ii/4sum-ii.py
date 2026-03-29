class Solution(object):
    def fourSumCount(self, arr1, arr2, arr3, arr4):
        mp={}
        for i in arr1 :
            for j in arr2:
                s=i+j
                if s in mp:
                    mp[s]+=1
                else:
                    mp[s]=1
                
        ans=0
        for k in arr3:
            for l in arr4:
                target= -(k+l)
                if target in mp :
                    ans+=mp[target]
        return ans


        