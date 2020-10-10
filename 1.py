# class PriorityQueue:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     def shift_up(self, i, e):
#         """pareNode = (curNode - 1) / 2"""
#         while i > 0:
#             parentNode = (i - 1) // 2
#             if self.stack[parentNode] < self.stack[i]:
#                 break
#             self.stack[i] = self.stack[parentNode]
#             i = parentNode
#
#         self.stack[i] = e
#
#     def add(self, e):
#         if e is None:
#             return
#         self.size += 1
#         self.stack.append(e)
#         self.shift_up(self.size - 1, e)
#
#     def poll(self):
#         pass
#
#
# test = PriorityQueue()
# test.add(1)
# test.add(2)
# test.add(4)
# test.add(3)
# test.add(0)
#
# print(test.stack)

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# def addTwoNumbers(self, l1, l2):
#
#     head = ListNode()
#     l3 = head
#     carry = 0
#     while l1 or l2:
#         if l1 and l2:
#             num = l1.val + l2.val + carry
#             carry = num // 10
#             ge = num % 10
#             l3.val = ge
#             l3.next = ListNode()
#             l3 = l3.next
#             l1 = l1.next
#             l2 = l2.next
#
#         if (not l1) and l2:
#             num = 0 + l2.val + carry
#             carry = num // 10
#             ge = num % 10
#             l3.val = ge
#             l3.next = ListNode()
#             l3 = l3.next
#             l2 = l2.next
#
#         if (not l2) and l1:
#             num = l1.val + 0 + carry
#             carry = num // 10
#             ge = num % 10
#             l3.val = ge
#             l3.next = ListNode()
#             l3 = l3.next
#             l1 = l1.next
#
#     return head
#
# result = []
#
#
# def dfs(n, k, tmp):
#     if k == 0:
#         result.append(list(tmp))
#
#         return
#
#     for i in range(n, 0, -1):
#         tmp.append(i)
#         dfs(i - 1, k - 1, tmp)
#         tmp.pop(-1)
#
#     return result
#
#
# print(dfs(4, 2, []))

# answer = []
# record = []
# candidates = [2,3,6,7]
# target = 7
#
#
# def dfs(candidates, target, record, last):
#     if target == 0:
#         answer.append(list(record))
#         print(record)
#         return
#
#     for i in range(last, len(candidates)):
#         if target >= candidates[i]:
#             record.append(candidates[i])
#             dfs(candidates, target - candidates[i], record, i)
#             record.pop(-1)
#
#
# dfs(candidates, target, record, 0)

# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#
#         if not word:
#             return
#
#         import copy
#
#         row = len(board)
#         col = len(board[0])
#         word_length = len(word)
#
#         visted = [[True for i in range(col)] for j in range(row)]
#
#         def dfs(visted, word_index, i, j):
#             if i < 0 or i >= row:
#                 return False
#
#             if j < 0 or j >= col:
#                 return False
#
#             if word_index >= word_length:
#                 return False
#
#             if visted[i][j]:
#                 if board[i][j] == word[word_index]:
#
#                     visted[i][j] = False
#
#                     if word_index == word_length - 1:
#                         return True
#
#                     a = dfs(visted, word_index + 1, i + 1, j)
#                     if a: return True
#                     b = dfs(visted, word_index + 1, i - 1, j)
#                     if b: return True
#                     c = dfs(visted, word_index + 1, i, j - 1)
#                     if c: return True
#                     d = dfs(visted, word_index + 1, i, j + 1)
#                     if d: return True
#
#                     visted[i][j] = True
#
#
#             return False
#
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j] == word[0]:
#                     if dfs(visted, 0, i, j):
#                         return True
#
#         return False

# class UnionFind:
#     def __init__(self, n):
#         self.ancestor = list(range(n))
#
#     def union(self, index1: int, index2: int):
#         self.ancestor[self.find(index1)] = self.find(index2)
#
#     def find(self, index: int) -> int:
#         if self.ancestor[index] != index:
#             self.ancestor[index] = self.find(self.ancestor[index])
#         return self.ancestor[index]
#
#
# class Demo(object):
#     def __init__(self, n):
#         self.arr = list(range(n))
#
#     # 找到祖父
#     def find(self, num):
#         if self.arr[num] != num:
#             self.arr[num] = self.find(self.arr[num])
#
#         return self.arr[num]
#
#     # 合并集合n到集合m
#     def union(self, n, m):
#         self.arr[self.find(n)] = self.find(m)
#
#
# arr = [[1,2], [2,3], [3,4], [4,1], [1,5]]
# length = len(arr)
#
# d = Demo(length + 1)
# a = UnionFind(length + 1)
#
# for _, (n1, n2) in enumerate(arr):
#     if d.find(n1) != d.find(n2):
#         d.union(n1, n2)
#
#     if a.find(n1) != a.find(n2):
#         a.union(n2, n1)
#     else:
#         print(n1, n2)
#
#
# print(a.find(4))
# print(a.find(1))
# print(a.find(2))
# print(a.find(3))
# print(a.find(5))

#
# class Solution(object):
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         answer = []
#
#         def dfs(start, length):
#
#             if length == start:
#                 answer.append(list(nums))
#
#             for i in range(start, length):
#
#                 if i + 1 < length and nums[i] == nums[i + 1]:
#                     continue
#                 nums[i], nums[start] = nums[start], nums[i]
#                 dfs(start + 1, length)
#                 nums[i], nums[start] = nums[start], nums[i]
#
#         dfs(0, len(nums))
#
#         return answer
#
#
# s = Solution()
# r = s.permuteUnique([2,2,1,1])
# print(r)
#
#

# class Solution(object):
#     def sumOfDistancesInTree(self, N, edges):
#         """
#         :type N: int
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#
#         length = len(edges) + 1
#         ans = []
#
#         data = [[] for i in range(length)]
#
#         # def get_data(n):
#         #     ans = []
#         #     for i in edges:
#         #         if i[0] == n:
#         #             ans.append(i[1])
#
#         #         elif i[1] == n:
#         #             ans.append(i[0])
#
#         #     return ans
#
#         for e in edges:
#             data[e[0]].append(e[1])
#             data[e[1]].append(e[0])
#
#         def dist(node, remove_number, n):
#             e = data[node]
#             ans = 0
#             for i in e:
#                 if i == remove_number:
#                     continue
#                 ans += 1 * n
#                 ans += dist(i, node, n + 1)
#             return ans
#
#         for i in range(length):
#             ans.append(dist(i, -1, 1))
#
#         return ans
#
#
# s = Solution()
#
#
# print(ans)

a = lambda x: (9 - x) // 2
arr = [" " * a(i) + "*" * i + " " * a(i) + "\n" for i in range(1, 10, 2)]
arr += arr[-2::-1]
s = "".join(arr)
print(s)