class Solution(object):
    def mergeAdjacent(self, arr):
        stack=[]

        for x in arr:
            while stack and stack[-1]==x:
                stack_top=stack.pop()
                x+= stack_top
            stack.append(x)

        return stack
            
        