class Solution(object):
    def is_prime(self,n):
        if n<=1:
            return False
        
        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                return False
            
        return True
    def sumOfPrimesInRange(self, n):
        num=n
        reverse=0
        while num!=0:
            reverse=reverse*10+(num%10)
            num=num//10
        start=min(reverse,n)
        end=max(reverse,n)
        total=0
        for i in range (start,end+1):
            if self.is_prime(i):
                total+=i
        return total
        

        
            
                        


        
        