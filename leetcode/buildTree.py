"""
106. 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        left_in = None
        right_in = None
        left_pos = None
        right_pos = None

        root_val = postorder.pop()
        loc = inorder.index(root_val)

        left_in = inorder[:loc]
        right_in = inorder[loc + 1:]
        left_pos = postorder[:loc]
        right_pos = postorder[loc:]

        root = TreeNode(root_val)
        root.left = self.buildTree(left_in, left_pos)
        root.right = self.buildTree(right_in, right_pos)

        return root
