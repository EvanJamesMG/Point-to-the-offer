/*
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
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
    boolean isSymmetrical(TreeNode pRoot)
    {
        if(pRoot==null)
            return true;
        return sym(pRoot.left,pRoot.right);
    }



    private boolean sym(TreeNode left, TreeNode right) {
        // TODO Auto-generated method stub
        if(left==null && right ==null)
            return true;
        if(left!=null&&right!=null&&left.val == right.val)
            return sym(left.left, right.right)&&sym(left.right, right.left);
        else 
            return false;
    }
}
