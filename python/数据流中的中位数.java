import java.util.ArrayList;
import java.util.Collections;
/*
题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
*/

public class Solution {

		ArrayList<Integer> input = new ArrayList<>();
	    public void Insert(Integer num) {
	    	input.add(num);
	    }

	    public  Double GetMedian() {
	    	Collections.sort(input);
	    	double res = 0;
	    	int length = input.size();
	    	if(length<=1){
	    		res = input.get(0);
	    		return res;
	    	}
	    	if(length%2==0)
		    	 res = (double)(input.get(length/2)+input.get(length/2-1))/2;	    		
	
	    	if(length%2==1)
		    	 res = input.get(length/2);	    		
	    	
	    	return res;	    		

	    }

}
