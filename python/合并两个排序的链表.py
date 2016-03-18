# coding=utf-8

__author__ = 'EvanJames'


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
合并链表,比较简单
'''


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        dummy = ListNode(0)
        newhead = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                newhead.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                newhead.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
            newhead = newhead.next
        if pHead1:
            newhead.next = pHead1
        if pHead2:
            newhead.next = pHead2
        return dummy.next
