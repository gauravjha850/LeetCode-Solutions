class Solution(object):
    def prime(self,num):
        if num <2 :
            return False
        for i in range (2,int(num**0.5)+1):
            if num % i == 0:
                return False
            
        return True
        



    def completePrime(self, num):
        if not self.prime(num):
            return False
        prefix=num//10
        while prefix >0:
            if not self.prime(prefix):
                return False
            prefix=prefix//10

        divisor=10
        while num> divisor:
            suffix=num%divisor
            if not self.prime(suffix):
                return False
            divisor=divisor*10
            
        return True


        