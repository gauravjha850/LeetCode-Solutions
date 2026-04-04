class Solution(object):
    def isHappy(self, n):
        def getnum(num):
            total=0
            while num>0:
                digit=num%10
                total=total+digit**2
                num=num//10
            return total
        slow=n
        fast=getnum(n)
        while fast != 1 and slow != fast :
            slow=getnum(slow)
            fast=getnum(getnum(fast))
        return fast==1

        