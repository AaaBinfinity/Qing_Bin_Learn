package D2分支结构;

/*用户选择
在实际开发中，如果我们需要在多种情况下选择其中一个，就可以使用switch语句。
当我们拨打了某些服务电话时，一般都会有按键选择。
假设现在我们拨打了一个机票预定电话。
电话中语音提示：
1机票查询
2机票预订
3机票改签
4退出服务
其他按键也是退出服务。请使用swtich模拟该业务逻辑。*/

import java.util.Scanner;

public class Practice用户选择 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("请输入按键");
        int n = in.nextInt();

        switch (n) {
            case 1:
                System.out.println("机票查询");
                break;
            case 2:
                System.out.println("机票预定");
                break;
            case 3:
                System.out.println("机票改签");
                break;
            case 4:
                System.out.println("退出服务");
                break;
            default:
                System.out.println("无效按键");
        }
    }
}
