# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        temp=head

        map_node=set()
        while temp is not None:
            if temp in map_node:
                return temp
            map_node.add(temp)
            temp=temp.next
        return None


        