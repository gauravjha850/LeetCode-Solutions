class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hash_map={}
        stack=[]
        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num= stack.pop()
                hash_map[smaller_num]=num

            stack.append(num)
        answer=[]

        for num in nums1:
            if num in hash_map :
                ans=hash_map[num]
            else:
                ans=-1
            answer.append(ans)
        
        return answer


        
        