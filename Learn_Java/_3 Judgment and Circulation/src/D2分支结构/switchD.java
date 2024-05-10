package D2分支结构;

/*switch语句格式

switch（表达式）{
case 值1:
语句体1;
break;
case 值2:
语句体2;
break;

...


default:
语句体n+1;
break;
}


格式说明：
I.    表达式：（将要匹配的值）
      取值为byte、short、int、char。
      JDK5以后可以是枚举，JDK7以后可以是String。
II.   case：后面跟的是要和表达式进行比较的值 （被匹配的值）
III.  break：表示中断，结束的意思，用来结束switch语句。
IV.   default: 表示所有情况都不匹配的时候，就执行该处的内容，
      和if语句的else相似。
V.    case后面的值只能是字面量，不能是变量
VI.   case给出的值不允许重复


 */


public class switchD {

    public static void main(String[] args) {
        //兰州拉面、武汉热干面、北京炸酱面、陕西油泼面
//1．定义变量记录我心里想吃的面
        String noodles = "兰州拉面";
//2．拿着这个面利用switch跟四种面条匹配
        switch (noodles) {
            case "兰州拉面":
                System.out.println("吃兰州拉面");
                break;
            case "武汉热干面":
                System.out.println("吃武汉热干面");
                break;
            case "北京炸酱面":
                System.out.println("吃北京炸酱面");
                break;
            case "陕西油泼面":
                System.out.println("吃陕西油泼面");
                break;
            default:
                System.out.println("吃方便面");
                break;
        }
    }
}
