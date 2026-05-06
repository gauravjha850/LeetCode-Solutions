# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_map={val: i for i,val in  enumerate(inorder)}
        self.pre_idx=0
        def helper(in_left,in_right):
            if in_left > in_right:
                return None
            root_val=preorder[self.pre_idx]
            root=TreeNode(root_val)
            self.pre_idx +=1
            mid=inorder_map[root_val]
            root.left=helper(in_left,mid-1)
            root.right=helper(mid+1,in_right)
            return root
        return helper(0,len(inorder)-1)


        