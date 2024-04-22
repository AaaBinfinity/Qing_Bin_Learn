package D1运算符;

import java.util.Scanner;

public class Practice数值拆分 {
    //需求：键盘录入一个三位数，将其拆分为个位、十位、百位后，打印在控制台
    public static void main(String[] args) {
        //1、键盘录入
        Scanner in= new Scanner(System.in);
        System.out.println("输入一个三位数：");
        int a = in.nextInt();
        //2、分别获取个位、十位、百位：
        int ge = a%10;
        System.out.println("个位："+ge);
        int shi = a/10%10;
        System.out.println("十位："+shi);
        int bai = a/100%10;
        System.out.println("百位："+bai);




    }

}
