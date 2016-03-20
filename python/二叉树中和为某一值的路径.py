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
'''
题目描述

输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

解题思路：DFS
注意坑：编程时候，valuelist.append(1)是对自己赋值，此时tem =valulist.append(1) 是不对的，
要想重新生成新的数组，应写为 valuelist+[1]
'''

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root == None:
            return []
        self.res = []
        self.DFS(root, expectNumber - root.val, [root.val])
        return self.res

    def DFS(self, root, expectNumber, valuelist):
        if root.left == None and root.right == None and expectNumber == 0:
            self.res.append(valuelist)
        if root.left:
            self.DFS(root.left, expectNumber - root.left.val, valuelist+[root.left.val])
        if root.right:
            self.DFS(root.right, expectNumber - root.right.val, valuelist+[root.right.val])

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = Solution().FindPath(root, 3)
    print(res)


'''
The fucking Java code!

import java.util.ArrayList;

public class test {
	
	public static void main(String[] args){
		
    	ArrayList<ArrayList<Integer>> res= new ArrayList<ArrayList<Integer>>();
    	TreeNode root = new TreeNode(1);
    	root.left = new TreeNode(2);
    	root.right = new TreeNode(3);
    	res= FindPath(root,4);
    	System.out.println(res);
		
	}
    public static ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
    	ArrayList<ArrayList<Integer>> res= new ArrayList<ArrayList<Integer>>();
    	if(root == null)
    		return res;
    	ArrayList<Integer> valuelist = new ArrayList<Integer>() ;
    	valuelist.add(root.val);
    	DFS(root,target-root.val,valuelist,res);
		return res;
        
    }

	private static void DFS(TreeNode root, int sum, ArrayList<Integer> valuelist, ArrayList<ArrayList<Integer>> res) {
		// TODO Auto-generated method stub
		if(root.left==null && root.right ==null && sum==0){
			res.add(valuelist);
		}
		if(root.left!=null){
			ArrayList<Integer> temlist = new ArrayList<Integer>(valuelist);
			temlist.add(root.left.val);
			DFS(root.left,sum-root.left.val,temlist,res);
		}
		if(root.right!=null){
			ArrayList<Integer> temlist = new ArrayList<Integer>(valuelist);
			temlist.add(root.right.val);
			DFS(root.right,sum-root.right.val,temlist,res);
		}
			
	}
}
'''
