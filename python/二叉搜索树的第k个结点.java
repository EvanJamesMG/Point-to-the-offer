/*
题目描述

给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。

public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
import java.util.ArrayList;

public class Solution {
    	ArrayList<TreeNode> reslist = new ArrayList<>();
	    TreeNode KthNode(TreeNode pRoot, int k)	{
	    	if(pRoot==null || k<=0)
	    		return null;
	    	midTravel(pRoot);
            if(k<=reslist.size())
	    		return reslist.get(k-1);
            return null;
	    }
		private void midTravel(TreeNode pRoot) {
			// TODO Auto-generated method stub
			if(pRoot!=null){
				if(pRoot.left!=null)
					midTravel(pRoot.left);
				reslist.add(pRoot);
				if(pRoot.right!=null)
					midTravel(pRoot.right);
			}
			
		}
}
