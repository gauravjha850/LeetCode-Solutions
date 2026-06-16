class Solution(object):
    def processStr(self, s):
        result=[]
        for word in s:
            if word.islower():
                result.append(word)
            elif word=='*':
                if result:
                    result.pop()
            elif word=='#':
                result=result+result
            
            elif word=='%':
                n=len(result)
                i=0
                j=n-1
                while i<j:
                    result[i],result[j]=result[j],result[i]
                    i+=1
                    j-=1
        return "".join(result)

        
        