class Solution(object):
    def nextGreaterElements(self, nums):
        stack=[]
        
        n=len(nums)
        result=[-1]*n
        for i in range(2*n-1,-1,-1):
            current_num=nums[i%n]
            while stack and stack[-1]<=current_num:
                stack.pop()
            if i<n:
                if stack:
                    result[i]=stack[-1]
                else:
                    result[i]=-1
            stack.append(current_num)


        return result


        