class Solution(object):
    def mySqrt(self, x):
        if x==0 :
            return 0
        if x==1:
            return 1
        low=0
        high=x//2
        ans=0
        while low<= high :
            mid=low+(high-low)//2
            if mid*mid== x:
                return mid
            elif mid*mid <= x :
                ans=mid
                low=mid+1
            else:
                high = mid-1
        return ans 

        