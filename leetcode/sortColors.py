"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


def sortColors_01(nums):
    """
    指针写法
    :param nums:
    :return:
    """
    p0 = i = 0
    p2 = len(nums) - 1

    while i < len(nums):

        while p0 < len(nums) and nums[p0] == 0:
            p0 += 1

        while p2 > -1 and nums[p2] == 2:
            p2 -= 1

        if nums[i] == 2 and i < p2:
            nums[p2], nums[i] = nums[i], nums[p2]
            p2 -= 1

        if nums[i] == 0 and i > p0:
            nums[p0], nums[i] = nums[i], nums[p0]
            p0 += 1

        i += 1


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    length = len(nums)
    p0 = 0
    p1 = 0

    for i in nums:
        if i == 0:
            p0 += 1
        elif i == 1:
            p1 += 1

    p1 += p0

    for i in range(length):
        if i < p0:
            nums[i] = 0

        elif i < p1:
            nums[i] = 1
        else:
            nums[i] = 2


