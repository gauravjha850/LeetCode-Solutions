class Solution(object):
    def mergeAdjacent(self, nums):
        stack=[]
        for num in nums :
            stack.append(num)

            while len(stack)>= 2 and stack[-1]==stack[-2]:
                sum_stack= stack.pop()+stack.pop()

                stack.append(sum_stack)
        return stack
        