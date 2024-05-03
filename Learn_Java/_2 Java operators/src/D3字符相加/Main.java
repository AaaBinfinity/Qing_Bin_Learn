package D3字符相加;

public class Main {
    //byte short char 三种类型的数据在运算的时候，都会直接先提升为int，然后再进行运算
    //但char是个字符啊？
    public static void main(String[] args) {
        char c ='a';  //字符＋字符或者字符＋数字时，会把字符通过ASCII码表查询到对应的数字再进行计算
        int r = c+0;
        System.out.println(r);

    }
}
