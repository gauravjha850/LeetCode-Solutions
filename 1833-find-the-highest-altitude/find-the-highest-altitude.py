class Solution(object):
    def largestAltitude(self, gain):
        maxi=0
        start=0
        for num in gain:
            start+= num
            
            maxi=max(start,maxi)
        return maxi
        