"""
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
输入：s = "1 + 1"
输出：2

输入：s = " 2-1 + 2 "
输出：3

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, num, sign = 0, 0, 1
        stack = []
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char == '+':
                ret += sign * num
                # 更新num, 开始获取下一个num
                num = 0
                # 更新符号
                sign = 1
            elif char == '-':
                ret += sign * num
                # 更新num, 开始获取下一个num
                num = 0
                # 更新符号
                sign = -1
            elif char == '(':
                # 先计算括号里的表达式, 同时保存之前的计算结果
                stack.append(ret)
                stack.append(sign)
                # 重新开始计算
                ret = 0
                sign = 1
            elif char == ')':
                # )前还有一个num需要计算
                ret += sign * num
                # 更新num
                num = 0
                # 括号里的表达式计算完成
                ret *= stack.pop()
                ret += stack.pop()
        # 末尾的num还没计算
        ret += sign * num
        return ret
