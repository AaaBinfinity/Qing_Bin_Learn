package D2数组的定义和静态初始化;

public class 数组的元素访问 {
    //格式：数组名[索引]
    public static void main(String[] args) {
        int[]arr1 = {11,12,13,14,15};
        //索引是从0 开始的

        //获取数组中0索引对应的数据并打印出来
        System.out.println(arr1[0]);

        //把数据储存到数组中
        //格式：   数组名[索引] = 具体的变量/数据

        arr1 [0] = 100;
        System.out.println(arr1[0]); //被覆盖掉了，原来的数据不存在了


    }
}
