class Solution(object):
    def findValidElements(self, nums):
        n = len(nums)
        if n == 0: return []
        
        is_valid = [False] * n
        stack = []
        left_max = float('-inf')
        
        for i in range(n):
            
            if nums[i] > left_max:
                is_valid[i] = True
                left_max = nums[i]
            
        
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            
            stack.append(i)
        
        
        for idx in stack:
            is_valid[idx] = True
            
        
        return [nums[i] for i in range(n) if is_valid[i]]
        