/*
输出常量
	printf（参数1，参数2）输出语句

参数1：必填，输出内容的最终样式以字符串的形式体现
参数2：选填，填补的内容
*/

/*
格式控制符(占位符)	说明	单词
整型				%d		decimal
实型				%f		floating-point
字符				%c      character
字符串				%s		string
*/

//输出一个整数
#include <stdio.h>
int main61()
{
	printf("%d", 12);
	return 0;
}
//输出小数
#include <stdio.h>
int main62()
{
	printf("李绮卿的年龄为：%f", 18.5);
	return 0;
}

//输出字符
//1.
#include <stdio.h>
int main63()
{
	printf("我的名字是李绮卿");
	return 0;
}

//2.
#include <stdio.h>
int main64()
{
	printf("我的名字是：%s", "李绮卿");
	return 0;
}



