class Solution(object):
    def countOppositeParity(self, nums):
        total_even=0
        total_odd=0
        for num in nums :
            if num%2==0:
                total_even+=1
            else:
                total_odd+=1
        seen_odd=0
        seen_even=0
        for i in range (len(nums)):
            current_val=nums[i]
            if current_val%2==0:
                nums[i]=total_odd-seen_odd
                seen_even+=1
            else:
                nums[i]=total_even - seen_even
                seen_odd+=1
        return nums
            

        
        