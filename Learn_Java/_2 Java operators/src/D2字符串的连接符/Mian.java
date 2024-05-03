package D2字符串的连接符;

public class Mian {
    public static void main(String[] args) {

        // 字符串的"+" 操作
        // 当 "+" 操作中出现字符串时，这个 "+" 是字符串连接符，而不是算术运算符了。会将前后的数据进行拼接，并产生一个新的字符串


        System.out.println("123" + 123); //123123 而不是246


        //连续进行"+"操作时，
        //从左到右逐个执行
        System.out.println(9 + 1 + "年营理");  //10年营理


        //只要有字符串出现就是拼接p

        int age = 18;
        System.out.println("我的年龄是" + "age" + "岁");
        System.out.println("我的年龄是" + age + "岁");


        System.out.println(1+2+"abc"+2+1);   //只要有字符串出现就是拼接  3abc21



    }
}
