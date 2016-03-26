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

输入两个链表，找出它们的第一个公共结点。
分析：
由于是单向链表的节点，每个节点只有一个next，因此从第一个公共节点开始，之后它们所有的节点都是重合的。
链表中的较长的一个先走多出的长度，之后两个链表一起走，找到共同的节点返回

'''


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        onehead = pHead1
        twohead = pHead2
        len1, len2 = 0, 0
        while onehead:
            len1 += 1
            onehead = onehead.next
        while twohead:
            len2 += 1
            twohead = twohead.next
        if len2>len1:
            for i in range(len2 - len1):
                pHead2 = pHead2.next
        else:
            for i in range(len1 - len2):
                pHead1 = pHead1.next
        while pHead1:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next


if __name__ == '__main__':
    pHead1 = ListNode(1)
    pHead1.next = ListNode(2)
    pHead1.next.next = ListNode(3)
    pHead2 = ListNode(2)
    pHead2.next = ListNode(3)
    res = Solution().FindFirstCommonNode(pHead1, pHead2)
    print(res)
