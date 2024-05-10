package D2分支结构;

public class Practice无人驾驶 {
    //红灯停绿灯行
    public static void main(String[] args) {
        boolean isLightGreen = false;
        boolean isLightYellow = false;
        boolean isLightRed = true;
        if (isLightGreen) {
            System.out.println("gogogo! ");
        }
        if (isLightYellow) {
            System.out.println("slow! ");
        }
        if (isLightRed) {
            System.out.println("stop! ");
        }
    }
}