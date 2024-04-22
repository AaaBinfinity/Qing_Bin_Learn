package D2分支结构;

import java.util.Scanner;

public class ifelse语句 {
/*

    If语句的第二种格式

    格式：
            if（关系表达式）{
        语句体1;
    }else {
        语句体2;
        }



        执行流程：
        I. 首先计算关系表达式的值
        II. 如果关系表达式的值为true就执行语句体1III．如果关系表达式的值为false就执行语句体2IV．继续执行后面的其他语句
*/

/*
    需求：键盘录入一个整数，表示身上的钱。
    如果大于等于100块，就是网红餐厅。
    否则，就吃经济实惠的沙县小吃。
*/
public static void main(String[] args) {
    System.out.println("身上有多少钱？");
    Scanner in = new Scanner(System.in);
    int m = in.nextInt();
    if (m>=100){
        System.out.println("网红餐厅");
    }else {
        System.out.println("沙县小吃");
    }

}


}
