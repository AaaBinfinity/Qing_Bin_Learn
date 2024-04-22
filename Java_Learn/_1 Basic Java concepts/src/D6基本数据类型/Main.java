package D6基本数据类型;
/*

基本数据类型


数据类型            关键字         取值范围
整数               byte          -128~127
                  short         -32768~32767
                  int           -2147483648~2147483647 (10位数）
                  long          -9223372036854775808~9223372036854775807(19位数）
浮点数             float          -3.401298e-38到3.402823e+38
                  double        -4.9000000e-324到1.797693e+308
字符               char          0-65535
布尔               boolean       true, false





*/



//字符串类型：String  （不是基本数据类型）


public class Main {
    public static void main(String[] args) {

        byte a = 10;
        System.out.println(a);
        short q = 20;
        System.out.println(q);

        int w = 123;
        System.out.println(w);
        long e = 123123213L; //long类型定义时后面要加上L
        System.out.println(e);
        float s = 102.1F; //foat类型在定义时后面要加上F
        System.out.println(s);
        double z = 12.12;
        System.out.println(z);
        char h = 'H';
        System.out.println(h);
        boolean x = true;
        System.out.println(x);

    }
}
