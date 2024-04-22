package D7逻辑运算符;

/*

在数学中，一个数据x，大于5，小于15，我们可以这样来进行表示：5<x<15
在Java中，需要把上面的式子先进行拆解，再进行合并表达。
拆解为：x>5和x<15
合并后：x>5&x<15  (且)

*/


/*


逻辑与（且）       并且 两边都为真，结果才是真      &
逻辑或           或者 两边都为假，结果才是假       |
逻辑异或          相同为 false，不同为true       ^
逻辑非             取反                        !



 */


/*
 短路运算符：
 场景：登录界面，用户名输入正确，需要判断密码；但用户名输入错误，就没必要判断密码了

 &&    短路与     结果和＆相同，但是有短路效果
 ||    短路或     结果和|相同，但是有短路效果


短路就是 不执行后边了（会提高运行效率）

 */




public class Main {
    public static void main(String[] args) {

        //1、  &   并且  两边都是真 结果才是真
        System.out.println(true & true);//true
        System.out.println(true & false);//false
        System.out.println(false & true);//false
        System.out.println(false & false);//false


        //2、 |  或者  两边都是假 结果才是假
        System.out.println(true | true);//true
        System.out.println(true | false);//true
        System.out.println(false | true);//true
        System.out.println(false | false);//false

        //场景：用户登录界面 账号和密码同时输入正确才能登录成功；就是“并且”；


        //3、 ^  异或  相同是假 不同是真   (联想异性才可以结婚)
        System.out.println(true ^true);//false
        System.out.println(true ^false);//true
        System.out.println(false^ true);//true
        System.out.println(false^ false);//false



        //4、 !   取反
        System.out.println(!false);//true
        System.out.println(!!false);//false




//        短路运算符：

//        短路与
        System.out.println(true && true);//true
        System.out.println(true && false);//false
        System.out.println(false && true);//false
        System.out.println(false && false);//false

//        短路或
        System.out.println(true || true);//true
        System.out.println(true || false);//true
        System.out.println(false || true);//true
        System.out.println(false || false);//false


      //  短路逻辑运算符具有短路效果
      //          简单理解：当左边的表达式能确定最终的结果，那么右边就不会参与运行


        int d = 10,c = 10;
        boolean res = ++d<5&&++c>5;
        System.out.println(res);//false
        System.out.println(d);
        System.out.println(c);//短路 不执行 所以是10






    }
}
