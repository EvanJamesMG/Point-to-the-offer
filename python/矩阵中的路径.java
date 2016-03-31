/*
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

DFS

*/
import java.util.ArrayList;
import java.util.Arrays;

/**
用一个状态数组保存之前访问过的字符，然后再分别按上，下，左，右递归
*/
public class Solution {
    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {
        int flag[] = new int[matrix.length];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (helper(matrix, rows, cols, i, j, str, 0, flag))
                    return true;
            }
        }
        return false;
    }
 
    private boolean helper(char[] matrix, int rows, int cols, int i, int j, char[] str, int k, int[] flag) {
        int index = i * cols + j;
        if (i < 0 || i >= rows || j < 0 || j >= cols || matrix[index] != str[k] || flag[index] == 1)
            return false;
        if(k == str.length - 1) return true;
        flag[index] = 1;
        if (helper(matrix, rows, cols, i - 1, j, str, k + 1, flag)
                || helper(matrix, rows, cols, i + 1, j, str, k + 1, flag)
                || helper(matrix, rows, cols, i, j - 1, str, k + 1, flag)
                || helper(matrix, rows, cols, i, j + 1, str, k + 1, flag)) {
            return true;
        }
        flag[index] = 0;
        return false;
    }
}



public class Solution {
	public  boolean hasPath(char[] matrix, int rows, int cols, char[] str){
	    if(matrix==null ||matrix.length==0)
	    	return false;
	    for(int i=0;i<rows;i++){
	    	for(int j=0;j<cols;j++){
	    		if(matrix[i*cols+j]==str[0]){
	    			 if(helper(matrix,i,j,rows,cols, Arrays.copyOfRange(str, 1, str.length)))
	    				 return true;
	    		}
	    	}
	    }
	return false;
	}

	    
	private  boolean helper(char[] matrix, int indexrows, int indexcols, int rows, int cols, char[] str) {
		// TODO Auto-generated method stub
		if(str.length==0)
			return true;
		//up
		if((indexrows>0)&&(matrix[(indexrows-1)*cols+indexcols]==str[0])){
			char tem =matrix[indexrows*cols+indexcols];
			matrix[indexrows*cols+indexcols]='#';
			if(helper(matrix, indexrows-1, indexcols, rows, cols, Arrays.copyOfRange(str, 1,str.length)))
				return true;
			matrix[indexrows*cols+indexcols]=tem;
		}
		//down	
		if(indexrows<rows-1&&matrix[(indexrows+1)*cols+indexcols]==str[0]){
			char tem = matrix[indexrows*cols+indexcols];
			matrix[indexrows*cols+indexcols] ='#';
			if(helper(matrix, indexrows+1, indexcols, rows, cols, Arrays.copyOfRange(str, 1,str.length)))
				return true;
			matrix[indexrows*cols+indexcols]=tem;
		}
		//left	
		if(indexcols>0&&matrix[indexrows*cols+indexcols-1]==str[0]){
			char tem = matrix[indexrows*cols+indexcols];
			matrix[indexrows*cols+indexcols]='#';
			if(helper(matrix, indexrows, indexcols-1, rows, cols, Arrays.copyOfRange(str, 1,str.length)))
				return true;
			matrix[indexrows*cols+indexcols]=tem;
		}
		//right
		if(indexcols<cols-1&&matrix[indexrows*cols+indexcols+1]==str[0]){
			char tem = matrix[indexrows*cols+indexcols];
			matrix[indexrows*cols+indexcols]='#';
			if(helper(matrix, indexrows, indexcols+1, rows, cols, Arrays.copyOfRange(str, 1,str.length)))
				return true;
			matrix[indexrows*cols+indexcols]=tem;
		}
		return false;
	}
}
