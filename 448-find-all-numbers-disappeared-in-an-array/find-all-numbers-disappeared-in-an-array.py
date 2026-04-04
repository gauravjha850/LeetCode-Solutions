class Solution(object):
    def findDisappearedNumbers(self,arr):
        num=set(arr)
        res=[]
        for i in range (1,len(arr)+1):
            if i  not in num:
                res.append(i)
        return res
          
        