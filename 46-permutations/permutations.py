class Solution(object):
    def permute(self, nums):
        n=len(nums)
        result=[]
        used=[False]*n
        def backtrack(current):
            if len(current) == n :
                result.append(current[:])
                return
            for i in range (n):
                if not used[i]:
                    used[i]=True
                    current.append(nums[i])
                    backtrack(current)
                    used[i]=False
                    current.pop()
        backtrack([])
        return result
        