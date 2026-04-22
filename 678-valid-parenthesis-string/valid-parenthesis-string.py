class Solution(object):
    
    def checkValidString(self, s):
        mini=0
        maxi=0
        for i in range(len(s)):
            if s[i]=='(':
                mini=mini+1
                maxi=maxi+1
            elif s[i]==')':
                mini=mini-1
                maxi=maxi-1
            else:
                mini=mini-1
                maxi=maxi +1
            if maxi<0:
                return False
            if mini<0:
                mini=0
        return mini == 0

            