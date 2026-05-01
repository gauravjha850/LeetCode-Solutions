class Solution(object):
    def absDifference(self, nums, k):
        nums.sort()
        return abs(sum(nums[:k])-sum(nums[-k:]))
        


        