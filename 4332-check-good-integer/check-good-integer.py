class Solution(object):
    def checkGoodInteger(self, n):
        squareSum=0
        digitSum=0
        while n!=0:
            digit=n%10
            squareSum+=digit**2
            digitSum+=digit
            n=n//10
        value=squareSum-digitSum
        return True if value>=50 else False
        
            

        
        