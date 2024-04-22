package D2分支结构;


//If语句的第三种格式


//        格式：
//        if
//        (关系表达式1){
//        语句体1;
//        } else if（关系表达式2){
//        语句体2;
//        }
//        ...
//        eles {
//        语句体 n + 1;
//        }


//        执行流程：
//        1．首先计算关系表达式1的值
//        II. 如果为true就执行语句体1；如果为false就计算关系表达式2的值
//        III．如果为true就执行语句体2；如果为false就计算关系表达式3
//        的值
//        IV.......
//        V. 如果所以关系表达式结果都为false，就执行语句体n+1。
//        else {
//        语句体 n + 1;


//从上往下依次进行判断只有要有一个判断为真， 就执行对应的语句体
//        如果所有的判断都为假， 就执行else的语句体

import java.util.Scanner;

public class elesif语句 {
    public static void main(String[] args) {
        System.out.println("成绩：");

        Scanner in = new Scanner(System.in);
        int score = in.nextInt();

        if (score > 0 && score <= 100) {
            if (score >= 95 && score <= 100) {
                System.out.println("送自行车一辆");
            } else if (score > 90 && score <= 94) {
                System.out.println("游乐场玩一天");
            } else if (score >= 80 && score <= 89) {
                System.out.println("送变形金刚一个");
            } else {
                System.out.println("揍一顿");
            }
        } else {
            System.out.println("无效值");
        }


    }


}
