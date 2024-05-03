package D3循环结构;

/*
需求：输入一个数x
如果x是一个回文数 打印true 反之打印false；


tips：
回文数是正序和倒序读都是一样的整数  例如 121 12321 123454321 234565432


 */


import java.util.Scanner;

public class Practice回文数 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("输入x的值：");
        int x = in.nextInt();
        int y = x;
        int num = 0;

        while (x != 0) {
            int g = x % 10;
            x /= 10;

            //获取倒序
            num = 10 * num + g;


        }

//到这儿x的值已经改变了 所以要再定义一个新的数来接收x的值

        System.out.println(num == y);
    }
}

