class Solution(object):
    def reversePrefix(self, s, k):
        char=list(s)
        left=0
        right=k-1
        while left<right:
            char[left],char[right] = char[right],char[left]
            left=left+1
            right=right-1
        return "".join(char)
        
        