"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)

        for i in range(length):
            diff = target - nums[i]

            try:
                j = nums.index(diff)

                if j != i:
                    return [i, j]
            except:
                pass

    def twoSum_2(self, nums, target):
        """
        创建哈希表解法

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        ans = None

        for i, v in enumerate(nums):
            diff = target - v

            if diff in dic:
                ans = [i, dic[diff]]
                break
            else:
                dic[v] = i

        return ans


