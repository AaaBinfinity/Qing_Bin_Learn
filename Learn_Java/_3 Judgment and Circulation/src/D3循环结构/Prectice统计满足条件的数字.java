package D3循环结构;

import java.util.Scanner;

public class Prectice统计满足条件的数字 {
/*
    需求：键盘录入两个数字，表示一个范围。统计这个范围中。
    既能被3整除，又能被5整除数字有多少个？
*/

    //统计的思想

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("请输入一个较小的数作为范围的较小值");
        int a = in.nextInt();
        System.out.println("请输入一个较大的数作为范围的较大值");
        int b = in.nextInt();
        int c = 0;
        for (int i = a; i <= b; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                c += 1;
            }
        }
        System.out.println(c);
    }
}
