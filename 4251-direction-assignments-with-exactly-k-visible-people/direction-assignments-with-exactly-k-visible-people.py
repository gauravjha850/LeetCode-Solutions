class Solution(object):
    mod=1000000007
    def nck(self,n,k):
        if k > n or k<0 :


            return 0
        elif k==n or k==0:
            return 1
        k=min(k,n-k)
        res=1
        for i in range (1,k+1):
            res=res*(n-i+1)//i
        return res% self.mod



    def countVisiblePeople(self, n, pos, k):
        t=self.nck(n-1,k)
        return ((2*t) % self.mod)


        
        
        
        
        