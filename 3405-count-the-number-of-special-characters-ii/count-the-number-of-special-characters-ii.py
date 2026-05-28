class Solution(object):
    def numberOfSpecialChars(self, word):
        low=[-1]*26
        high=[-1]*26
        for i,char in enumerate(word):
            if char.islower():

                ascii_idx=ord(char)-ord('a')
                low[ascii_idx]=i
            else:
                ascii_idx=ord(char)-ord('A')

                if high[ascii_idx]==-1:
                    high[ascii_idx]=i
        special_count=0
        for j in range (26):
            if low[j]!=-1 and high[j]!=-1:
                if low[j] < high[j]:
                    special_count+=1
        return special_count
        
        