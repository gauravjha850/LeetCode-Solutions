class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum={}
        current_sum=0
        count=0
        for i in range (len(nums)):
            current_sum+=nums[i]
            if current_sum==k:
                count+=1
            rem=current_sum-k
            if rem in prefix_sum:
                count+=prefix_sum[rem]
            if current_sum not in prefix_sum:
                prefix_sum[current_sum]=1
            else:
                prefix_sum[current_sum]+=1
        return count
            
            
        