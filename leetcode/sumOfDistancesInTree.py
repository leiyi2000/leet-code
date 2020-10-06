"""
834. 树中距离之和
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。

第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。

返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释:
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
"""


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        状态转移方程推导过程:
            ans(A) = sum(A) + sum(B) + count(B)
            ans(B) = sum(A) + sum(B) + count(A)
            N = count(A) + count(B)
            ans(A) = ans(B) + N - 2 * count(A)
        """

        data = [[] for i in range(N)]
        ans = [0] * N
        count = [1] * N

        for e in edges:
            data[e[0]].append(e[1])
            data[e[1]].append(e[0])

        def get_count(node, right):
            for i in data[node]:
                if i != right:
                    get_count(i, node)
                    count[node] += count[i]

        def dist(node, right, n):
            ans = 0
            for i in data[node]:
                if i != right:
                    ans += 1 * n
                    ans += dist(i, node, n + 1)

            return ans

        def dfs(node, right):
            for i in data[node]:
                if i != right:
                    ans[i] = ans[node] + N - 2 * count[i]
                    dfs(i, node)

        ans[0] = dist(0, -1, 1)
        get_count(0, -1)
        dfs(0, -1)

        return ans
