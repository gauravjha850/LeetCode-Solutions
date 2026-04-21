class Solution(object):
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()
        left=0
        right=0
        m=len(s)
        n=len(g)
        while left< n and right < m:
            if g[left]<=s[right]:
                left=left+1
            right=right+1
        return left
