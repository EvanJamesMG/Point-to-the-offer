'''
题目描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

1.将左子树构造成双链表，并返回链表头节点。
2.定位至左子树双链表最后一个节点。
3.如果左子树链表不为空的话，将当前root追加到左子树链表。
4.将右子树构造成双链表，并返回链表头节点。
5.如果右子树链表不为空的话，将该链表追加到root节点之后。
6.根据左子树链表是否为空确定返回的节点。
'''


class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return None
        if pRootOfTree.left == None and pRootOfTree.right == None:
            return pRootOfTree
        # 1.将左子树构造成双链表，并返回链表头节点。
        left = self.Convert(pRootOfTree.left)
        p = left
        # 2.定位至左子树双链表最后一个节点。
        while p and p.right:
            p = p.right
        # 3.如果左子树链表不为空的话，将当前root追加到左子树链表。
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p
        # 4.将右子树构造成双链表，并返回链表头节点。
        right = self.Convert(pRootOfTree.right)
        # 5.如果右子树链表不为空的话，将该链表追加到root节点之后。
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        # 6.根据左子树链表是否为空确定返回的节点。
        if left:
            return left
        else:
            return pRootOfTree
