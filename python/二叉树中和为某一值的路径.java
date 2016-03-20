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
