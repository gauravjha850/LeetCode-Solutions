class Solution(object):
    def numberOfSpecialChars(self, word):
        lower=[-1]*26
        upper=[-1]*26

        for i,char in enumerate(word):
            if char.islower():
                ascii_idx=ord(char)-ord('a')
                lower[ascii_idx]=i
            else:
                ascii_idx=ord(char)-ord('A')
                if upper[ascii_idx]==-1:
                    upper[ascii_idx]=i
        special_count=0
        for i in range (26):
            if lower[i]!=-1  and upper[i]!=-1 :
                if lower[i]<upper[i]:
                    special_count +=1
        return special_count
        
        