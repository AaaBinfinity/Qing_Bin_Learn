package D4自增自减运算符;

public class Main {

    /*

    符号     作用      说明
    ++       加     变量值加一
    --       减     变量值减一

    */


    public static void main(String[] args) {

        //++与--
        int a = 10;
        System.out.println(a); //10
        a++;
        System.out.println(a); //11
        ++a;
        System.out.println(a); //12
        a--;
        System.out.println(a); //11
        --a;
        System.out.println(a); //10


        //++和-- 既可以放在变量的前边，也可以放在变量的后边

        //参与计算

//        a++先用后加，++a先加后用；


//++在前：先加 后用
        int d = 12;

        int s = ++d;
        System.out.println(s);

//++在后：先用 后加
        int p = 12;
        int l = p++;
        System.out.println(l);


    }

}
