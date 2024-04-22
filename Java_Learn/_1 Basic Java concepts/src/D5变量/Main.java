package D5变量;


//变量：使用时总要改变的量

/*

假设一个场景：
登录界面，我们要拿用户输入的东西去跟正确的账号和密码做对比；
用户的输入就可以定义为变量
*/

public class Main {

    /*
格式：
    数据类型 变量名 = 数据值;
*/


    /*
     数据类型      关键字
       整数        int
      浮点数      double
     */



    public static void main(String[] args) {
//     定义变量：     数据类型 变量名 = 数据值;

//    数据类型：限定了变量能存储数据的类型
//     int（整数） double（小数）

//     变量名：就是存储空间的名字
//     作用：方便以后使用

//     数据值：真正存在变量中的数据
//     等号：赋值。把右边的数据赋值给左边的变量
        int a = 1;

//变量的使用方法：
//Tip：变量名不能被重复定义
        // 1、打印输出
        System.out.println(a);      //1

    //2、参与计算



    int w = 2;
    int e = 3;
        System.out.println(w+e);     //5

    //3、修改记录的值；
    int r = 12;
        System.out.println(r);      //12
        //修改成34：
        r = 34;
        System.out.println(r);       //34



/**
        * 注意事项 ：
        * 只能存一个值
        * 变量名不允许重复定义
        * 一条语句可以定义多个变量
        * 变量在使用之前一定要进行赋值
**/



//一条语句可以定义多个变量：
        int s = 45,d = 67,f = 89;
        System.out.println(s);
        System.out.println(d);
        System.out.println(f);






    }
}
