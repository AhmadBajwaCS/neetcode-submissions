# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    out = True
    def dfs_binarytree(self, node:Optional[TreeNode]):
        if not node:
            return 0

        print("first visit", node.val, "")

        left_height = self.dfs_binarytree(node.left)
        right_height = self.dfs_binarytree(node.right)

        print("second visit", node.val, "leftHeight: ", left_height, "vs", "rightHeight: ", right_height)
 
        if abs(left_height - right_height) >1:
            self.out = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # at every node. we need to calculate total height at that point.
        # if the height differs then we need to call it. 
        # essentially we are measuring how deep each node is. 

        self.dfs_binarytree(root)
        return self.out

        

    

        



