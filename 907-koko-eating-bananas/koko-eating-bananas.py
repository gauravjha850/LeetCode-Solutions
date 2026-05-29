class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        
        while low< high:
            mid=low+(high-low)//2
            total=0
            for pile in piles:
                total+=(pile+mid-1)//mid
            if total <= h:

                high=mid
            else:
                low=mid+1
        return low
                
        