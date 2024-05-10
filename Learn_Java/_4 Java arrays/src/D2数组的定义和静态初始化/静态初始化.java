package D2数组的定义和静态初始化;

public class 静态初始化 {

    //    初始化：就是在内存中，为数组容器开辟空间，并将数据存入容器中的过程
//    完整格式：数据类型[]数组名＝new数据类型[]{元素1，元素2，元素3..…}
    //简化格式：数据类型[]数组名＝{元素1，元素2，元素3.…};
    public static void main(String[] args) {
//    完整格式
        int[] array1 = new int[]{12, 1, 33, 333, 4653, 76354, 349};

        //简化格式
        int[] array2 = {12, 1, 33, 333, 4653, 76354, 349};
        //长度是7

        System.out.println(array2);//[I@3b6eb2ec  这个是数组的地址值
    }

}
