class Solution(object):
    def threeSum(self, arr):
        ans=[]
        arr.sort()
        for i in range(len(arr)):
            if i > 0 and arr[i]==arr[i-1]:
                continue
            left=i+1
            right=len(arr)-1
            while left<right:
                result = arr[i]+arr[left]+arr[right]
                if result == 0:
                    ans.append([arr[i],arr[left],arr[right]])
                    left=left+1
                    right=right-1





                    while left<right and arr[left]==arr[left-1]:
                        left=left+1
                    while left<right and arr[right]==arr[right+1]:
                        right=right-1
                elif result>0:
                    right=right-1
                else:
                    left=left+1
        return ans
                

                    
        
        