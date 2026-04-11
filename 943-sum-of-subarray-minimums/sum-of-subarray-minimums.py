class Solution(object):
    def next_smaller_element(self,arr):
        n=len(arr)
        res=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                res[i]=n
            else:
                res[i]=stack[-1]

            stack.append(i)
        return res
    def previous_smaller_equal(self,arr):
        n=len(arr)
        stack=[]
        res=[-1]*n
        for i in range (n):
            
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                res[i]=-1
            else:
                res[i]=stack[-1]
            stack.append(i)
        return res
                
    

    def sumSubarrayMins(self, arr):
        total=0
        mod=int(1e9 + 7)
        pse=self.previous_smaller_equal(arr)
        nse=self.next_smaller_element(arr)
        n=len(arr)
        for i in range (n):
            left=i-pse[i]
            right=nse[i]-i
            freq=(right*left*1)
            value=(freq*arr[i])%mod
            total=(total+value)%mod
        return total
        





        
        