class Solution(object):
    def permute(self, nums):
        result=[]

         
        def back(temp):
            
            if len(nums)==len(temp):
                result.append(temp[:])
                return
            for num in nums :
                if num in temp:
                    continue
                temp.append(num)

                back(temp)

                temp.pop()
        back([])

        return result


        