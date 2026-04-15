class Solution(object):
    def bloom_days(self,bloomDay,day,m,k):
        count=0
        bouquets=0
        for bloom in bloomDay:
            if bloom <=day :
                count =count+1
                if count ==k:
                    bouquets=bouquets+1

                    count =0
            else:
                count=0
        return bouquets>=m
        
    def minDays(self, bloomDay, m, k):
        if m*k > len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=5
        while low <= high :
            mid= low+(high-low)//2
            

            if self.bloom_days(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 
        



        