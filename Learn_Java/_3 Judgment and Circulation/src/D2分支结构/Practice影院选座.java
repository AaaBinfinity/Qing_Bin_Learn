package D2分支结构;

//电影院选座也会使用到if判断。
// 假设某影院售卖了100张票，票的序号为1~100。
// 其中奇数票号坐左侧，偶数票号坐右侧。
// 键盘录入一个整数表示电影票的票号。
// 根据不同情况，

// 给出不同的提示：
// 如果票号为奇数，那么打印坐左边
// 如果票号为偶数，那么打印坐右边。

import java.util.Scanner;

public class Practice影院选座 {
    public static void main(String[] args) {
        System.out.println("请输入票号：");
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        if (a >= 0 && a <= 100) {
            if (a % 2 == 0) {
                System.out.println("坐在右侧座位");
            } else {
                System.out.println("坐在左侧作为");
            }
        }else {
            System.out.println("无效");
        }

    }
}
