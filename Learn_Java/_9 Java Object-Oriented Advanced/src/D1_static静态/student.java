package D1_static静态;

public class student {
    //属性：姓名、年龄、性别
    private String name;
    private int age;
    private String gender;
    public static String teacher;

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getGender() {
        return gender;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void syudy(){
        System.out.println(name+
                "正在学习"  );
    }

  public void show(){
      System.out.println(name);
      System.out.println(gender);
      System.out.println(age);
      System.out.println(teacher);
  }
}
