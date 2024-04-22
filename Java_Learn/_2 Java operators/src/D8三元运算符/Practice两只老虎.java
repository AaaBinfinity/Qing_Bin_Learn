package D8三元运算符;

import java.util.Scanner;

public class Practice两只老虎 {
    /* 需求：动物园里有两只老虎，体重分别为通过键盘录入获得，
请用程序实现判断两只老虎的体重是否相同。*/
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("第一只老虎的重量：");
        int a = in.nextInt();
        System.out.println("第二只老虎的重量：");
        int b = in.nextInt();

        String result = a==b?"相同":"不同";
        System.out.println(result);
    }
}
