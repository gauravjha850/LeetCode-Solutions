class Solution(object):
    def countVowelSubstrings(self, word):
        vowels="aeiou"
        n=len(word)
        count=0
        left=0
        mid=0
        freq={}
        for right in range(n):
            ch=word[right]
            if ch not in vowels:
                freq.clear()
                left=right+1
                mid=right+1
                continue
            if ch in freq :
                freq[ch]+=1
            else:
                freq[ch]=1
            while len(freq)==5:
                
                left_ch=word[left]
                freq[left_ch]-=1
                if freq[left_ch]==0:
                    del freq[left_ch]
                left=left+1
            count+=(left-mid)
        return count
                
        