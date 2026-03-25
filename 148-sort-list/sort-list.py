# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next :
            return head
        
        
        arr=[]
        temp=head
        while temp!=None:

            arr.append(temp.val)
            temp=temp.next
        
        arr=self.merge_sort(arr)


        temp=head
        i=0
        while temp!=None :
            temp.val=arr[i]
            temp=temp.next
            i=i+1
        return head
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        mid= len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge_arr(left,right)
    def merge_arr(self,left,right) :
        result =[]
        i = j = 0

        while i < len(left) and j < len(right) :


            if left[i] <= right[j]:

                result.append(left[i])
                i=i+1
            
            else :



                result.append(right[j])
                j=j+1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


        

        

        