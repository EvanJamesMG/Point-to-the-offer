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
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点）。

思路：
1.根据原始链表的每个节点N创建对应的N',把N'连接在N的后面
2.设置复制出来的结点的随机指针
3.把这个长链表拆分为两个链表，按照奇偶数
'''

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return pHead
        self.CloneNodes(pHead)         # 复制节点
        self.ClonerandomPointer(pHead) # 复制随机指针
        return self.Reconnect(pHead)   # 把两个连接的链表拆分

    def CloneNodes(self, pHead):
        currenthead = pHead
        while currenthead:
            self.clonehead = RandomListNode(currenthead.label)
            self.clonehead.next = currenthead.next
            currenthead.next = self.clonehead
            currenthead = self.clonehead.next

    def ClonerandomPointer(self, pHead):
        currenthead = pHead
        while currenthead:
            self.clonehead = currenthead.next
            if currenthead.random:
                self.clonehead.random = currenthead.random.next
            currenthead = self.clonehead.next

    def Reconnect(self, pHead):
        pCloneHead = pHead.next
        currNode = pHead
        while currNode.next:
            tmp = currNode.next
            currNode.next = tmp.next;
            currNode = tmp
        return pCloneHead


if __name__ == '__main__':
    res = Solution().Clone()
    print(res)
