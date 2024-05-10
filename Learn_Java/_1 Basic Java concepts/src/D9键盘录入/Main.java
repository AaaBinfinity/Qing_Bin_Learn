package D9键盘录入;
//Scanner类

//步骤一： 导包 --- 找到Scanner这个类在哪:
import java.util.Scanner;  //这个要写在定义类的上方；



public class Main {
    public static void main(String[] args) {
        System.out.println("输入一个整数：");
        //步骤二： 创建对象 --- 表示我要开始用Scanner这个类了
        Scanner a = new Scanner(System.in);  //这个“a”可以是任何名字

        //步骤三：接收数据 --- 真正开始干活了;
        int i = a.nextInt();
        System.out.println(i);


    }
}
