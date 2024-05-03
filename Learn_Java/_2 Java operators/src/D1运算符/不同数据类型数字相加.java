package D1运算符;
//数字进行运算时，数据类型不一样不能运算，需要转成一样的才能运算

//隐式转换（自动类型提升）:取值范围小的数值--->>取值范围大的数值
//强制转换：取值范围大的数值--->>取值范围小的数值

//byte < short < int < long < float < double

public class 不同数据类型数字相加 {
    public static void main(String[] args) {


        //隐式转换


        int a = 1; //(自动类型提升成double了)
        double b = 1.1;
        double c = a+b; //c是double
        System.out.println(c);

        int f = 3;//(自动类型提升成double了)
        double t = 4.00;
        double r = f+t;
        System.out.println(r);


        //byte short char 三种类型的数据在运算的时候，都会直接先提升为int，然后再进行运算
        byte u = 2;
        byte o = 9;
        int w = u+o;
        System.out.println(w);



        int i = 10;
        long n = 100L;
        double y = 20.0;
        double re = i + n + y;  //从左到右依次进行计算；
        System.out.println(re);




        //强制转换

        //如果把一个取值范围大的数值，赋值给取值范围小的变量。是不允许直接赋值的。
        // 如果一定要这么做就需要加入强制转

        // 格式：目标数据类型 变量名＝（目标数据类型）被强转的数据；


        int v= 1;
        v = (int) 3.0;   //强制转换
        System.out.println(v);

        byte b1 = 10;
        byte b2 = 21;
        byte l = (byte) (b1+b2); //他们要提升到int 所有要强制转换
        System.out.println(l);





    }
}
