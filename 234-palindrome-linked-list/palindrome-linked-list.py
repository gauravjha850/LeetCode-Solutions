# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp=head
        map_node=[]
        while temp is not None :
            map_node.append(temp.val)
            temp=temp.next
        temp=head
        while temp is not None :
            if (temp.val !=map_node[-1]):
                return False
            map_node.pop()
            temp=temp.next
        return True
            
        