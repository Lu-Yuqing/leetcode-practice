# Problem Link:https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# method 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0]) # the first element in preorder is root
        mid = inorder.index(preorder[0]) # find the root position in inorder
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid]) #build left subtree, preorder decides the tree structure
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) # build right subtree
        return root

# T: O(N^2)
# S: O(N^2)
# When build a tree, use preorder to identify the root, use inorder to identify which elements in left and right subtree.