package D2分支结构;

//If语句在程序中就是用来进行判断的

import java.util.Scanner;

public class if语句 {
    public static void main(String[] args) {

/*


        格式：

        if（关系表达式）{
            语句体；
         }


         执行流程：
            I. 首先计算关系表达式的值
            II. 如果关系表达式的值为true就执行语句体
            III. 如果关系表达式的值为false就不执行语句体
            IV．继续执行后面的其他语句


*/
        Scanner in = new Scanner(System.in);
        System.out.println("a = ");
        int a = in.nextInt();
        if (a>10){
            System.out.println("a比10大");
        }//只有一句代码，大括号可以省略，但不建议


        //布尔值

        boolean f = true;
        if (f){
            System.out.println("Binfinity");
        }




    }
}
