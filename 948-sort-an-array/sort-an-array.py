class Solution(object):
    def sortArray(self, arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=self.sortArray(arr[:mid])
        right=self.sortArray(arr[mid:])
        return self.merge(left,right)
    def merge(self,left,right):
        i=0
        j=0
        result=[]
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1
        result.extend(left[i:])
        result.extend(right[j:])
        return result        