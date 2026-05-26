class Solution(object):
    def largestNumber(self, nums):
        str_arr=[str(num) for num in nums]

        sorted_nums=self.merge_sort(str_arr)

        result="".join(sorted_nums)

        return "0" if result[0]=="0" else result
    def merge_sort(self,arr):
        
        if  len(arr)<=1:
            return arr
        
        
        mid=(len(arr))//2
        left_half=self.merge_sort(arr[:mid])
        right_half=self.merge_sort(arr[mid:])
        return self.merge(left_half,right_half)
    def merge(self,left,right):
        merged=[]
        i=0
        j=0

        while i < len(left) and j< len(right):
            if left[i]+right[j]> right[j]+left[i]:
                merged.append(left[i])
                i=i+1
            else:
                merged.append(right[j])
                j=j+1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged       