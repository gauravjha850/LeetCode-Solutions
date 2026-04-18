class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        doubled=s+s
        return goal in doubled 
        
        