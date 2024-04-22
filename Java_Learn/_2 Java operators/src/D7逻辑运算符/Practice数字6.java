package D7逻辑运算符;

import java.util.Scanner;

public class Practice数字6 {
    //数字6是一个真正伟大的数字，键盘录入两个整数。
    //如果其中一个为6，最终结果输出true。
    //如果它们的和为6的倍数。最终结果输出true。
    //其他情况都是false。

    public static void main(String[] args) {
//        分析：
//1．键盘录入两个整数
//变量a 变量b
//2.a==6 b==6 (a + b)%6==0
//如果满足其中一个，那么就可以输出true

        Scanner in = new Scanner(System.in);
        System.out.println("a=");
        int a = in.nextInt();
        System.out.println("b=");
        int b = in.nextInt();
      boolean res=  a==6|| b == 6|| (a+b)%6==0;
        System.out.println(res);
    }
}
