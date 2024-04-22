package D1_static静态;

public class Test{
    public static void main(String[] args) {
        student s1 = new student();
        //加了static之后可以这样调用：
        student.teacher = "ninini";
        s1.setAge(21);
        s1.setGender("男");
        s1.setName("binfinity");
        s1.syudy();
       // s1.teacher = "ithm";
        s1.show();

        student s2 = new student();
        s2.setAge(22);
        s2.setGender("男");
        s2.setName("cb");
        s2.syudy();
        s2.show(); //不加static是null

    }
}
