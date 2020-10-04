"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        node = head
        overflow = 0

        while l1 and l2:
            sum_ = l1.val + l2.val + overflow
            node.next = ListNode(sum_ % 10)
            overflow = sum_ // 10
            l1, l2 = l1.next, l2.next
            node = node.next

        while l1:
            sum_ = l1.val + overflow
            node.next = ListNode(sum_ % 10)
            overflow = sum_ // 10
            node = node.next
            l1 = l1.next

        while l2:
            sum_ = l2.val + overflow
            node.next = ListNode(sum_ % 10)
            overflow = sum_ // 10
            node = node.next
            l2 = l2.next

        if overflow:
            node.next = ListNode(overflow)

        return head.next
