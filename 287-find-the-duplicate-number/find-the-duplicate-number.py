class Solution(object):
    def findDuplicate(self, arr):
        slow=arr[0]
        fast=arr[0]
        while  True :
            fast=arr[arr[fast]]
            slow=arr[slow]
            if fast == slow :
                break
        slow=arr[0]
        while fast != slow:
            fast=arr[fast]
            slow=arr[slow] 
            
        return fast

        


        
        