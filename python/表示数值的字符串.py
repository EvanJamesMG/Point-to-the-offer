/*
  题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

没意思的题啊
*/


public class Solution {
	public boolean isNumeric(char[] str) {
		
		try {
			double re = Double.parseDouble(new String(str));
		} catch (Exception e) {
			// TODO: handle exception
			return false;
		}
		return true;
	}
}
