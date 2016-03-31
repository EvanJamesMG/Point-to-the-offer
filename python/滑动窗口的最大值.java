/*
题目描述

给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

*/
import java.util.ArrayList;
import java.util.Arrays;
public class Solution {
        public static ArrayList<Integer> maxInWindows(int [] num, int size)
        {
			ArrayList<Integer> res= new ArrayList<>();
			if(num==null ||num.length==0|| size==0)
				return res;
			int length = num.length;
			for(int i=0;i<length-size+1;i++){
				int [] tem;
				int maxnum = Integer.MIN_VALUE;
		        tem = Arrays.copyOfRange(num, i, i+size);
		        for(int j=0;j<size;j++){
		        	if(tem[j]>maxnum)
		        		maxnum = tem[j];
		        }
		        res.add(maxnum);
			}
        	
        	return res;
            
        }
}
