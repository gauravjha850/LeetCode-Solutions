 
class Solution(object):
    def permute(self, nums):
        result_list=[]
        def back(temp_list):
            if len(temp_list)==len(nums):
                result_list.append(list(temp_list))
                return
            
            for num in nums :
                if num in temp_list:
                    continue
                temp_list.append(num)

                back(temp_list)

                temp_list.pop()

        back([])

        return result_list
        
        