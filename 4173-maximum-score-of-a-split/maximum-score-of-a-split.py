class Solution(object):
    def maximumScore(self, nums):
        n=len(nums)
        suffix_min=[0]*n
        suffix_min[-1]=nums[-1]
        for i in range (n-2,-1,-1):
            suffix_min[i]=min(nums[i],suffix_min[i+1])
        max_score= float('-inf')
        current_prefix_sum=0
        for i in range(n-1):
            current_prefix_sum +=nums[i]

            score=current_prefix_sum-suffix_min[i+1]
            max_score=max(score,max_score)
        return max_score

        