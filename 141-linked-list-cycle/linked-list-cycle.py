# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        temp=head
        map_node={}
        while temp is not None  :
            if temp in map_node:
                return True
            map_node[temp]=1
            temp=temp.next
        return False
            
