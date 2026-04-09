class Solution(object):
    def mirrorDistance(self, n):
        def reverse(n):

            ulta=0
            while n!=0 :
                remain=n%10
                ulta=ulta*10+ remain
                n=n//10
            return ulta
        reversed_n=reverse(n)
        return abs(n-reversed_n)
        