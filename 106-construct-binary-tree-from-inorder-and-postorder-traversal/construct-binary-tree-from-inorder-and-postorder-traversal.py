# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        inorder_map={val:i for i,val in enumerate(inorder)}
        self.postorder_idx=len(postorder)-1
        def helper(in_left,in_right):
            if  in_left> in_right:
                return None
            root_val=postorder[self.postorder_idx]
            root=TreeNode(root_val)
            self.postorder_idx-=1
            mid=inorder_map[root_val]
            
            root.right=helper(mid+1,in_right)
            root.left=helper(in_left,mid-1)
            return root
        return helper(0,len(inorder)-1)

        
        