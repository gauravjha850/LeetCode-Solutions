class Solution(object):
    def lengthOfLongestSubstring(self, s):
        keep=set()
        max_count=0
        i=0
        for j in range (len(s)):
            while s[j]  in keep:
                keep.remove(s[i])
                i+=1
            keep.add(s[j])

            current_count=j-i+1
            max_count=max(current_count,max_count)
        return max_count
                

        