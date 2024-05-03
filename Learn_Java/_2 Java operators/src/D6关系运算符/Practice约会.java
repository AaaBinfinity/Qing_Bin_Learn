package D6关系运算符;
import java.util.Scanner;

public class Practice约会 {

    /*
    和约会对象在餐厅里面正在约会
键盘录入两个整数，表示你和你约会对象衣服的时髦度（手动录入0~10之间的整数，不能录其他）
如果你的时髦程度大于你对象的时髦程度，相亲就成功，输出true。
否则输出false。
*/

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("我的时尚值：");
        int m = in.nextInt();
        System.out.println("她的时尚值：");
        int h = in.nextInt();
        System.out.println(m>h);



    }
}
