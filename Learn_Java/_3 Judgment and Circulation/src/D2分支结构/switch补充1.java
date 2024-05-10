package D2分支结构;


/*
*
* case穿透
*       就是语句体里面没写break导致的；
*
*
*
* 执行流程：
首先还是会拿着小括号中表达式的值跟下面每一个case进行匹配。
如果匹配上了，就会执行对应的语句体，如果此时发现了break，那么结束整个switch语句。
如果没有发现break，那么程序会继续执行下一个case的语句体，一直遇到break或者右大括号为止。
*
*
*
* */

import java.util.Scanner;

//抽奖 随机输入一个三位数 有一等奖 二等奖和三等奖
public class switch补充1 {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        System.out.println("请输入一个三位整数：");

        int a = in.nextInt();
        switch (a) {
            case 321:
            case 435:
            case 654:
                System.out.println("一等奖");
                break;
            case 543:
            case 345:
            case 631:
                System.out.println("二等奖");
                break;
            case 438:
            case 545:
            case 875:
                System.out.println("三等奖");
                break;
            default:
                System.out.println("未中奖");
                break;

        }


    }
}
