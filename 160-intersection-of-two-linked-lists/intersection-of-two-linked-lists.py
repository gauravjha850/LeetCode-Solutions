# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        listA=headA
        listB=headB

        while listA !=listB :
            if listA is not None :
                listA=listA.next
            else:
                listA=headB
            if listB is not None :
                listB=listB.next
            else:
                listB=headA
        return listA
        