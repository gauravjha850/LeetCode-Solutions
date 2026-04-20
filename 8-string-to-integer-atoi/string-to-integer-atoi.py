class Solution(object):
    def myAtoi(self, s):
        if not s :
            return 0
        int_max=2**31 -1
        int_min= -2**31
        i=0
        n=len(s)
        while i < n and s[i] ==' ':
            i=i+1
        if i==n:
            return 0
        sign=1
        if s[i]=='+':
            i=i+1
        elif s[i]=='-':
            sign=-1
            i=i+1
        res=0
        while i < n and s[i].isdigit():
            digit=int(s[i])
            res=res*10+digit
            if res*sign <= int_min :
                return int_min
            if res*sign >= int_max :
                return int_max 
            i=i+1
        return res*sign
            
            

        