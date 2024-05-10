package D5变量;

public class Practice {
    public static void main(String[] args) {
//        有一辆公交车，一开始没有乘客
        int c = 0;

//        第一站：上去一位乘客
        c = c + 1;
//        第二站：上去两位乘客，下来一位乘客
        c = c + 2 - 1;

//    第三站：上去两位乘客，下来一位乘客
        c = c - 1 + 2;
        //   第四站：下来一位乘客
        c -= 1;
//        第五站：上去一位乘客
        c += 1;
//        请问：到了终点站，车上一共几位乘客。
        System.out.println("到了终点站，车上一共" + c + "位乘客");

    }
}
