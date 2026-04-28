class Solution(object):
    def validDigit(self, n, x):
        digit=str(n)
        if int(digit[0])==x:
            return False
        count=0
        for i in range (1,len(digit)):
            if int(digit[i])==x:
                count+=1
                break
        return count >0


            

        