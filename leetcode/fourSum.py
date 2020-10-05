"""
18. 四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        ans = []
        self.length = len(nums)

        def binarySearch(arr, l, r, x):
            """
            二分查找优化
            :param arr: 查找数组
            :param l: 左边起始位置
            :param r: 右边起始位置
            :param x: 查找值
            :return: 返回查找成功的下标 -1为查找失败
            """
            if r >= l:
                mid = (l + r) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    return binarySearch(arr, l, mid - 1, x)
                else:
                    return binarySearch(arr, mid + 1, r, x)
            else:

                return -1

        def dfs(start, t, tar, n):
            """

            :param start: 起始位置
            :param t: 临时数组保存
            :param tar: 目标值
            :param n: 记录次数
            :return:
            """
            if n == 3:
                index = binarySearch(nums, start, self.length - 1, tar)
                if index != -1:
                    t.append(tar)
                    ans.append(list(t))
                    t.pop()
                return

            if n > 3:
                return

            for i in range(start, self.length):
                # 剪枝
                if tar - (4 - len(t)) * nums[-1] > 0:
                    return
                if tar - nums[i] * (4 - len(t)) < 0:
                    return

                if i > start and nums[i - 1] == nums[i]:
                    continue

                t.append(nums[i])
                dfs(i + 1, t, tar - nums[i], n + 1)
                t.pop()

        dfs(0, [], target, 0)

        return ans
