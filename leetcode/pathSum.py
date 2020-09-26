"""
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

解题思路： dfs+回溯
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(root, sum, tmp):
            if root is None:
                return

            if root.left is None and root.right is None and sum == root.val:
                tmp.append(root.val)
                ans.append(list(tmp))
                tmp.pop()
                return

            tmp.append(root.val)
            dfs(root.left, sum - root.val, tmp)
            dfs(root.right, sum - root.val, tmp)
            tmp.pop()

        dfs(root, sum, [])

        return ans
