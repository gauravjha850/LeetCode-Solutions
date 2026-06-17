class Solution(object):
    def permuteUnique(self, nums):
        n=len(nums)
        nums.sort()
        result=[]
        used=[False]*n
        def back(temp):
            if len(temp)==n:
                result.append(temp[:])
                return 
            for i in range (n):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not  used[i-1]:
                    continue
                used[i]=True
                temp.append(nums[i])
                back(temp)
                temp.pop()
                used[i]=False
        back([])
        return result



        
        