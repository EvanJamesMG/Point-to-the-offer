'''
题目描述

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, preorder, inorder):
        # write code here
        
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.reConstructBinaryTree(preorder[1 : index + 1], inorder[0 : index])
        root.right = self.reConstructBinaryTree(preorder[index + 1 : len(preorder)], inorder[index + 1 : len(inorder)])
        return root
