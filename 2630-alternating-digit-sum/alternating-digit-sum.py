class Solution(object):
    def alternateDigitSum(self, n):
        digit=[]
        while n >0:
            digit.append(n%10)
            n=n//10
        digit.reverse()
        total_even = 0
        total_odd = 0
        for i in range (len(digit)):
            
            if i%2==0:
                total_even+=(digit[i])
            else:
                total_odd+=(digit[i])
        return total_even - total_odd
            

        
        
            
                
        