class Solution(object):
    def isUgly(self, n):
        if n <=0:
            return False
        for num in [2,3,5]:
            while n%num==0:
                n//=num
        return n==1


        