/*
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
*/

import java.util.ArrayList;
public class Solution {
    public int[] multiply(int[] a) {
        
        if(a==null||a.length==0)
            throw new RuntimeException("Your arr is invalid!");
        int len = a.length;
        int[] b = new int[len];
        b[0] = 1;
        // 自左至右将A[0]*A[1]*...*A[i-1]的结果存于先存于数组b[i]
        for (int i = 1; i < b.length; i++) {
            b[i] = b[i-1]*a[i-1];
        }
        int acc = 1;
        // 自右自左构建A[i+1]*A[i+2]*...*A[n-1]并累乘到b[i]
        for (int j = b.length-2; j >=0 ; j--) {
            acc*=a[j+1];
            b[j] = acc*b[j];
        }
        return b;      

    }
}
