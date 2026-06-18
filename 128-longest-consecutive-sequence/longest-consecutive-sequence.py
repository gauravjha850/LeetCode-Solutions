class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        max_count=0
        for num in s :
            if num -1 not in s:
                value=num+1
                current_count=1
                while value in s:
                    current_count+=1
                    value+=1
                max_count=max(current_count,max_count)
        return max_count

        
        