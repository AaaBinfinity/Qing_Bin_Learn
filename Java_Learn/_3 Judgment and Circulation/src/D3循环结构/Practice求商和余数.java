package D3循环结构;

/*
需求：给定两个整数，被除数和除数（都是正数，且不超过int的范围）
将两数相除，要求不使用乘法、除法和 ％运算符。
得到商和余数。
*/

import java.util.Scanner;

public class Practice求商和余数 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("输入被除数：");
        int a = in.nextInt();
        System.out.println("输入除数：");
        int b = in.nextInt();
        int c = 0;
        while (a >= b) {
            a = a - b;
            c++;
        }
        System.out.println("商为" + c + " ，余数为" + a);
    }
}