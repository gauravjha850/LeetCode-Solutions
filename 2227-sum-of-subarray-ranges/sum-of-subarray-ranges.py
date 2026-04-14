class Solution(object):
    def next_smaller_element(self,arr):
        n=len(arr)
        stack=[]
        result=[n]*n
        for  i in range (n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                result[i]=n
            else:
                result[i]=stack[-1]
            stack.append(i)
        return result
    def prev_smaller_element(self,arr):
        n=len(arr)
        stack=[]
        result=[-1]*n
        for  i in range (n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if not stack:
                result[i]=-1
            else:
                result[i]=stack[-1]
            stack.append(i)
        return result
    def next_greater_element(self,arr):
        n=len(arr)
        stack=[]
        result=[n]*n
        for  i in range (n-1,-1,-1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if not stack:
                result[i]=n
            else:
                result[i]=stack[-1]
            stack.append(i)
        return result
    def prev_greater_element(self,arr):
        n=len(arr)
        stack=[]
        result=[-1]*n
        for  i in range (n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if not stack:
                result[i]=-1
            else:
                result[i]=stack[-1]
            stack.append(i)
        return result
    def sum_of_subarray_minimum(self,arr):
        pse=self.prev_smaller_element(arr)
        nse=self.next_smaller_element(arr)
        total=0
        mod=int(1e9 + 7)
        n=len(arr)
        for i in range (n):
            left=i-pse[i]
            right=nse[i]-i

            freq=((left*right))
            value=(freq*arr[i])
            total=(total+value)
        return total
    def sum_of_subarray_maximum(self,arr):
        pse=self.prev_greater_element(arr)
        nse=self.next_greater_element(arr)
        total=0
        mod=int(1e9 + 7)
        n=len(arr)
        for i in range (n):
            left=i-pse[i]
            right=nse[i]-i

            freq=((left*right))
            value=(freq*arr[i])
            total=(total+value)
        return total


    def subArrayRanges(self,arr):
        return (self.sum_of_subarray_maximum(arr)-self.sum_of_subarray_minimum(arr))

        