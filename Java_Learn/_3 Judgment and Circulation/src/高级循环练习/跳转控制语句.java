package 高级循环练习;

public class 跳转控制语句 {
    public static void main(String[] args) {

        for (int i = 1;i<=10;i++){
            if (i == 2){
                System.out.println("小猫不吃巧克力");
                //结束本次循环 继续下一次循环
                continue;
            }

            if(i==5){
                System.out.print("小猫吃饱了，");
                //结束本次循环 也不继续下次循环
                break;
            }



            System.out.println("小猫在吃第" +i+
                    "罐罐头");
        }

        System.out.print("小猫走了");
    }
}
