"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""
"""
官方解法，还在研究ing，只知道递归。。。
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res


作者：LeetCode - Solution
链接：https: // leetcode - cn.com / problems / binary - tree - postorder - traversal / solution / er - cha - shu - de - hou - xu - bian - li - by - leetcode - solution /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。