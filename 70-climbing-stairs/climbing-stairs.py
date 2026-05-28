class Solution(object):
    def climbStairs(self, n):
        if n<=3:
            return n
        first=2
        second=3
        for _ in range (4,n+1):

            first,second=second,first+second
        return second 
        
        