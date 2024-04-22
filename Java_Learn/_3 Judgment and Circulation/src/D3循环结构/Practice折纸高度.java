package D3循环结构;

/*打印折纸的次数

需求：世界最高山峰是珠穆朗玛峰（8844.43米＝8844430毫米），
假如我有一张足够大的纸，它的厚度是0.1毫米。
请问，我折叠多少次，可以折成珠穆朗玛峰的高度？
*/

public class Practice折纸高度 {
    public static void main(String[] args) {

        int c = 0;
        double h = 0.1;
        while (h < 8844430) {
            h *= 2;
            c++;
        }
        System.out.println(c);

    }
}
