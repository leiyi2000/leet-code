"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 我的解决答案
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = {}

        def dfs(root):
            if root is None:
                return

            if root.val in data:
                data[root.val] += 1
            else:
                data[root.val] = 1

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        ans = None
        max_count = 0

        for k, v in data.items():
            if max_count < v:
                max_count = v
                ans = [k, ]
            elif max_count == v:
                ans.append(k)

        return ans


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 官方思路

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.pre = None
        self.count = 0
        self.max_count = -1
        self.ans = []

        def dfs(root):
            if root is None:
                return

            dfs(root.left)

            if self.pre is None:
                self.count = 1

            elif self.pre.val == root.val:
                self.count += 1
            else:
                self.count = 1

            self.pre = root

            if self.count == self.max_count:
                self.ans.append(root.val)
            elif self.count > self.max_count:
                self.ans = [root.val, ]
                self.max_count = self.count

            dfs(root.right)

        dfs(root)
        return self.ans
