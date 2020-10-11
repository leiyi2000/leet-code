"""
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].


示例 2:

输入: [1, 2, 3, 5]

输出: false
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = sum(nums)

        if sum1 & 1:
            return False

        target = sum1 // 2

        if target < max(nums):
            return False

        n = len(nums)

        # 动态规划
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            # 0...i 全部不选 (nums[0] + ....+ nums[i] = 0)
            dp[i][0] = True

        # 选第0个
        dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    # 不选 | 选
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]

                else:
                    # 超过了j 只能不选
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]

        # 超时代码
        # sum1 = sum(nums)

        # if sum1 & 1:
        #     return False

        # nums.sort(reverse=True)
        # target = sum1 // 2

        # if nums[0] > target:
        #     return False

        # def dfs(nums, target):

        #     if target == 0:
        #         return True

        #     elif target < 0:
        #         return False

        #     for i in range(start, len(nums)):
        #         # 剪枝
        #         if i > start and nums[i] == nums[i-1]:
        #             continue

        #         # 元素
        #         target -= nums[i]

        #         # 找到一个成立就停止递归
        #         if dfs(target, i + 1):
        #             return True

        #         target += nums[i]

        # return dfs(nums, target)
