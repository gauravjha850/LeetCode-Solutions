class Solution(object):
    def isIsomorphic(self, s, t):
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        map_st={}
        map_ts={}
        for i in range (n):
            char_s=s[i]
            char_t=t[i]
            if char_s in map_st :
                if map_st[char_s]!=char_t:

                    return False
            if char_t in map_ts :
                if map_ts[char_t]!=char_s:

                    return False
            map_st[char_s]=char_t
            map_ts[char_t]=char_s
        return True
        
        