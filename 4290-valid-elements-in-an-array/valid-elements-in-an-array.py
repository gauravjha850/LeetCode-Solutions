class Solution(object):
    def findValidElements(self, nums):
        n=len(nums)
        if n==0:
            return []
        stack=[]
        winners=set()
        left_max=float('-inf')
        for i in range (n):
            current=nums[i]
            if current > left_max :
                winners.add(i)
                left_max=current
            while stack and current >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        winners.update(stack)
        result =[]
        for i in range(n):
            if i in winners :
                result.append(nums[i])
        return result


        
        