package D6关系运算符;
/*

a == b，判断a和b的值是否相等，成立为true，不成立为false
a != b，判断a和b的值是否不相等，成立为true，不成立为false
a > b，判断a是否大于b，成立为true，不成立为false
a >= b，判断a是否大于等于b，成立为true，不成立为false
a < b，判断a是否小于b，成立为true，不成立为false
a <= b，判断a是否小于等于b，成立为true，不成立为false

        */


//Tip：关系运算符的结果都是boolean类型，要么是true，要么是false    千万不要把"=="误写成"="。

public class Main {
    public static void main(String[] args) {
        //1、== 判断左右两边是否相等
        int a = 1, b = 1, c = 2;
        System.out.println(a == b);
        System.out.println(a == c);


    }
}
