package D5赋值运算符;


/*

符号                  =                  +=                     -=                     *=                 /=                  %=
作用                 赋值               加后赋值                减后赋值                 乘后赋值           除后赋值             取余后赋值
说明      int a=10，将10赋值给变量a     a+=b，将a+b的值给a     a-=b，将a-b的值给a     a*=b，将a*b的值给a   a/=b，将a÷b的商给a     a%=b，将a÷b的余数给a

tip：他们其实在运行的时候会用强制类型转换
*/

public class Main {
    public static void main(String[] args) {

//        举个栗子
        //+=   将左边和右边进行相加，然后再把结果赋值给左边
        int a = 10;
        int b = 20;
        a += b;
        System.out.println(a);
        System.out.println(b);

    }
}
