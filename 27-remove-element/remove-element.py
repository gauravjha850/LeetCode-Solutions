class Solution(object):
    def removeElement(self, nums, val):
        good_value=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[good_value]=nums[i]
                good_value +=1
        return good_value


        

        