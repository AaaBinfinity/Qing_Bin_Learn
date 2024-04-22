package D1运算符;
/**
 * 运算符
 * 对字面量或者变量进行操作的符号

 * 表达式
 * 用运算符把字面量或者变量连接起来，符合java语法的式子就可以称为表达式。
 * 不同运算符连接的表达式体现的是不同类型的表达式。
 */
public class Main {
    public static void main(String[] args) {
        //算数运算符
        int a =6;
        int b = 3;
//        加
        System.out.println(a+b);
//        减
        System.out.println(a-b);
//        乘
        System.out.println(a*b);
//        除
        System.out.println(a/b);
        System.out.println(b/a);//只有整数参与计算结果只能是整数
//        取模 取余
        System.out.println(a%b);
        System.out.println(b%a);

/*
        应用场景：


        1．可以用取模来判断，A是否可以被B整除
        A % B 10 % 3


        2．可以判断A是否为偶数
        A % 2 如果结果为0．那么证明A是一个偶数。如果结果为1，那么证明A是一个奇数


        3．在以后，斗地主发牌
                三个玩家
        把每一张牌都定义一个序号
        拿着序号％3 如果结果为1，就发给第一个玩家。
        如果结果为2，那么就发给第二个玩家
        如果结果为0，那么就发给第三个玩家*/



//Tip：如果在运算中有小数的参与，结果有可能不精确
        System.out.println(1.1+1.01);


    }
}
