import java.awt.Label;
import java.awt.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
/*
题目描述

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
*/
/*
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
	    public static ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
	        LinkedList<TreeNode> mlist = new LinkedList<>();
	        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
	        if(pRoot==null)
	    		return res;
	    	mlist.add(pRoot);
	    	while(mlist.size()!=0){
	    		ArrayList<Integer> temlist = new ArrayList<>();
	    		int length = mlist.size();
	    		for(int i=0;i<length;i++){
		    		TreeNode temnode = mlist.pop();
		    		temlist.add(temnode.val);
		    		if(temnode.left!=null)
		    			mlist.add(temnode.left);
		 
		    		if(temnode.right!=null)
		    			mlist.add(temnode.right);
	    		}
		    	res.add(temlist);
	    	}
			return res;
	    }
}
