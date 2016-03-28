/*
题目描述

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

考虑二进制加法的过程，

步骤一、A^B，能够得到没有进位的加法。

步骤二、A&B，能够得到相加之后，能够进位的位置的信息。向左移动一位，就是两个二进制数相加之后的进位信息。所以，(A&B)<<1就是两个二进制数相加得到的“进位结果”。

步骤三、将前两步的结果相加。相加的过程就是步骤一和步骤二，直到不再产生进位为止。
*/
public class Solution {
    public int Add(int num1,int num2) {
        int n1;
        int n2;
        do{
            n1 = num1 ^ num2;
            n2 = (num1 & num2)<<1;
            num1 = n1;
            num2 = n2;
        }while(num2 !=0);
        
        return n1;
    }
        
}
