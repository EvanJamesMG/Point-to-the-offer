# coding=utf-8

__author__ = 'EvanJames'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


'''
题目描述
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

丑陋数序列可以拆分为下面3个子列表：

(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
我们可以发现每一个子列表都是丑陋数本身(1, 2, 3, 4, 5, …) 乘以 2, 3, 5

接下来我们使用与归并排序相似的合并方法，从3个子列表中获取丑陋数。每一步我们从中选出最小的一个，然后向后移动一步。
'''
class Solution:
    def GetUglyNumber_Solution(self, index):

        if index==0:
            return 0
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < index:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += [m]
        return q[-1]


