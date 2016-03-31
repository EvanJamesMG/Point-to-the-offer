/*题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
序列化是将二叉树转化为字符串，反序列化是将字符串转为二叉树
这里采用的是先序遍历
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
	    static String str = "";
		private static int index=-1;
	    static String Serialize(TreeNode root) {
		    doit(root);
		    return str;
	    }
	    private static void doit(TreeNode root) {
			// TODO Auto-generated method stub
	    	if(root!=null){
	    		str+=Integer.toString(root.val)+",";
	    		doit(root.left);
	    		doit(root.right);
	    	}else{
	    		str+="#,";	    		
	    	}
		}

		static TreeNode Deserialize(String str) {
	        index++;
	        int len = str.length();
	        if(index >= len){
	            return null;
	        }
	        String[] strr = str.split(",");
	        TreeNode node = null;
	        if(!strr[index].equals("#")){
	            node = new TreeNode(Integer.valueOf(strr[index]));
	            node.left = Deserialize(str);
	            node.right = Deserialize(str);
	        }
	         
	        return node;
	    }
}
