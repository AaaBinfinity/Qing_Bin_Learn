package D3循环结构;

/*
格式：
初始化语句；
while（条件判断语句）{
循环体语句；
条件控制语句；
}
*/

/*
执行流程：
① 执行初始化语句
② 执行条件判断语句，看其结果是true还是false
如果是false，循环结束
如果是true，执行循环体语句
③ 执行条件控制语句
④ 回到②继续执行条件判断语句
*/


//和for循环一模一样


/*
for 和 while 的区别：
> for循环中：知道循环次数或者循环的范围
> while循环：不知道循环的次数和范围，只知道循环的结束条件。
**/

public class while循环 {
    public static void main(String[] args) {
        //用while循环打印1-100；
        int i = 1;
        while (i<=100){
            System.out.println(i);
i++;

        }

    }
}
