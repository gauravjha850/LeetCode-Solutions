class Solution(object):
    def countOperations(self, num1, num2):
        if num1==num2:
            return 0 if num1==0 else 1       
        count=0
        while (num1 !=0 and num2 !=0):
            
            if num1 >= num2 :
                
                count += num1//num2
                num1=num1%num2
            elif num1<=num2:
                
                count+=num2//num1
                num2=num2%num1
        return count


        