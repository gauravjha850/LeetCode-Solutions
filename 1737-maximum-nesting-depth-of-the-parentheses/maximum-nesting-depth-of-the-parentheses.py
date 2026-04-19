class Solution(object):
    def maxDepth(self, s):
        count=0
        max_count=0
        for char in s :
            if char == '(' :
                count=count+1
                if count > max_count :

                    max_count =count 
            elif char==')':
                count=count-1
        return max_count
        