class Solution(object):
    def reverse(self, x):
        rev=0
        
        sign=-1 if x < 0 else 1
        x=abs(x)
        while x!=0:
            rev=rev*10 + x%10
            x=x//10
        rev=rev*sign

        return rev if (-(1 << 31) <= rev <= (1 << 31) -1 ) else 0
        