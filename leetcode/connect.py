"""
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。



进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 我的方法
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return

        stack = [root, ]
        next_stack = []

        while stack or next_stack:

            while stack:
                tmp = stack.pop(0)
                tmp.next = stack[0] if stack else None

                if tmp.left:
                    next_stack.append(tmp.left)

                if tmp.right:
                    next_stack.append(tmp.right)

            stack = next_stack
            next_stack = []

        return root

    """
    按照官方思路自己写的一个递归
    """


class Solution_01(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        head = root
        connect_head = head_next = Node(None)
        """
        这里做了一个优化
        """
        # while head and not head_next:
        #     if head.left:
        #         head_next = head.left
        #         connect_head = head.left
        #     elif head.right and not head_next:
        #         connect_head = head.right
        #         head_next = head.right
        #
        #     if head.left and head.right and head_next:
        #         head_next.next = head.right
        #         head_next = head_next.next
        #
        #     head = head.next

        while head:
            if head.left:
                head_next.next = head.left
                head_next = head_next.next

            if head.right:
                head_next.next = head.right
                head_next = head_next.next

            head = head.next

        self.connect(connect_head.next)

        return root
