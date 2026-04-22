class Solution(object):
    def bulbSwitch(self, n):
        i =1
        count=0
        while i**2 <= n:
            count =count+1
            i=i+1
        return count
        
        