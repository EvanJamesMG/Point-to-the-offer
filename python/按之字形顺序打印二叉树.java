import java.awt.Label;
import java.awt.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;

/*
题目描述
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
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
	    	int index=0;
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
	    		index++;

	    		if(index%2==1){
		    		res.add(temlist);

	    		}else{
	    			Collections.reverse(temlist);
		    		res.add(temlist);
	    		}
	    	}
	    	
			return res;

	    }

}
