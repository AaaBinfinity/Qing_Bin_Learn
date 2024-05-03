package D4字面量;

public class Main {

    //字面量：告诉程序员数据在程序中的书写格式

    //字面量类型：
    //整数类型、小数类型   直接写就行 10   1.11
    // 字符串类型  用双引号括起来    "Binfinity"
    // 字符类型    用单引号括起来，内容只能有一个    '你'  '0'  'q'
    // 布尔类型   布尔值，表示真假        只有两个值：true、false
    // 空类型     一个特殊的值，空值         值是  null

    //特殊的字符类型的字面量：
    //  \t  制表符：在打印的时候，把前面字符串的长度补齐到8，或者8的整数倍。最少补1个空格，最多补8个空格。


    public static void main(String[] args) {

        //常见的数据在代码中书写：

        //整数
        System.out.println(328);

        //小数
        System.out.println(1.1);

        //字符串
        System.out.println("Binfinity!");

        //字符
        System.out.println('男');

        //布尔
        System.out.println(true);

        //空
        //tip：null是不能直接打印的；
        //蜀国我们想打印null，只能用字符串的形式进行打印
        System.out.println("null");

        //  \t; 可以用来让数据对齐
        System.out.println("name     " + '\t' + "age");
        System.out.println("Binfinity" + '\t' + "18");


        //制表符的基本用法：
        System.out.println("name     " + '\t' + "age");
        System.out.println("Binfinity" + '\t' + "18");
        System.out.println("mom     " + '\t' + "48");
        System.out.println("father  " + '\t' + "50");

    }

}
