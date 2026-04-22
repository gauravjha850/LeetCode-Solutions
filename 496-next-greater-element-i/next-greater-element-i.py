class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hash_map={}
        ans=[]
        stack=[]
        for num in nums2:
            while stack and stack[-1]< num :
                smaller=stack.pop()
                hash_map[smaller]=num
            stack.append(num)
        for num in nums1:
            if num in hash_map:
                answer=hash_map[num]
            else:
                answer=-1
            ans.append(answer)
        return ans

                
        