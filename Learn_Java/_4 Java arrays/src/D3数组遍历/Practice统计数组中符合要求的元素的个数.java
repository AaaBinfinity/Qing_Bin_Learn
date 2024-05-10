package D3数组遍历;

public class Practice统计数组中符合要求的元素的个数 {

    //定义一个数组，存储1,2,3,4,5,6,7,8,9,10
    //遍历数组得到每一个元素，统计数组里面一共有多少个能被3整除的数字
    public static void main(String[] args) {
        int j = 0;
        int [] arr={1,2,3,4,4,5,6,7,8,9,10};
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]%3==0){j++;
            }
        }
        System.out.println(j);

    }
}
