package D2分支结构;

//假设，用户在超市实际购买，商品总价为：600元。
//键盘录入一个整数表示用户支付的钱
//如果付款大于等于600，表示付款成功。否则付款失败。

import java.util.Scanner;

public class Practice商品付款 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("请付款");
     int   a  = in.nextInt();
     if (a>=600){
         System.out.println("支付成功");
     }else {
         System.out.println("支付失败");
     }


        System.out.println();
    }

}
