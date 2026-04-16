class Solution(object):
    def reverseWords(self, s):
        word=s.split()
        result=[]
        for i in range (len(word)-1,-1,-1):
            result.append(word[i])
            
            if i != 0:
                result.append(' ')
        return "".join(result)
            
    


        


        