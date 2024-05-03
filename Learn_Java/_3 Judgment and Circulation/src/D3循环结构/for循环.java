package D3循环结构;


//for循环

/*
格式：
for(初始化语句;条件判断语句;条件控制语句){
循环体;
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

public class for循环 {
    //输出10次“你好”:
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.println("你好");
        }

    }

}
