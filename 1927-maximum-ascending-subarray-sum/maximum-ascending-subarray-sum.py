class Solution(object):
    def maxAscendingSum(self, arr):

        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=arr[0]
        current_sum=arr[0]
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                current_sum+=arr[i]
            else:
                current_sum=arr[i]
            max_sum=max(current_sum,max_sum)
        return max_sum       