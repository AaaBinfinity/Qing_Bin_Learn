package D8三元运算符;


import java.util.Scanner;

//
//作用：可以进行判断，根据判断的结果得到不同的内容
//格式：关系表达式?表达式1:表达式2;
public class Main {
    public static void main(String[] args) {
        //需求：定义一个变量记录两个整数的较大值。
        Scanner in = new Scanner(System.in);
        System.out.println("a=");
        int a = in.nextInt();
        System.out.println("b=");
        int b = in.nextInt();
//判断“a比b大吗？” 真输出a 假输出b
        System.out.println(a > b ? a : b);
    }

}
