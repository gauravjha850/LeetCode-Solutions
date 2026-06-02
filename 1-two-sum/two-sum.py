class Solution(object):
    def twoSum(self, nums, target):
        mp={}
        for i in range (len(nums)):
            needed=target-nums[i]
            if needed in mp :
                return [mp[needed],i]
            mp[nums[i]]=i

        