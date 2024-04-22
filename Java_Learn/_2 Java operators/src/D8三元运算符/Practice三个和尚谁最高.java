package D8三元运算符;

/*
一座寺庙里住着三个和尚，已知他们的身高分别为150cm、210cm、165cm,请用程序实现获取这三个和尚的最高身高。
*/

import java.util.Scanner;

public class Practice三个和尚谁最高 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("第一个和尚的身高：");
        int a = in.nextInt();
        System.out.println("第二个和尚的身高：");
        int b = in.nextInt();
        System.out.println("第三个和尚的身高：");
        int c = in.nextInt();

        //先比较前两个 再把高的跟第三个比较
        int temp = a > b ? a : b;
        int he = temp > c ? temp : c;
        System.out.println(he);

    }
}
