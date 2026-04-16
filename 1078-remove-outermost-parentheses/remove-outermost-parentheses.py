class Solution(object):
    def removeOuterParentheses(self, s):
        result=[]
        stack_len=0
        for ch in s :
            if ch =='(':
                if stack_len > 0:
                    result.append(ch)
                stack_len+=1
            else:
                stack_len-=1
                if stack_len>0:
                    result.append(ch)
        return "".join(result)
            


        