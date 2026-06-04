class Solution(object):
    def majorityElement(self, nums):
        candi=None
        count=0
        for num in nums :
            if count==0:
                candi=num
            if candi==num:
                count+=1
            else:
                count-=1
        return candi



        
        