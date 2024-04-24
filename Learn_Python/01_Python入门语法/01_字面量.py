print(888)  # 888
print("8-2")  # 8-2
print('8-2')  # 8-2
print(8 - 2)  # 6
# print('8'-'6')    字符串不能相减
print("caobin ")
print(True)
print(False)

# CTRL+ALT+L	代码格式标准化

8
1.232
"徐静"
'5'
True
False

"""
注意！！Python程序严格考究字符的缩进和大小写
"""

'''

pycharm快捷键：

        一、代码编辑快捷键
    
    1	CTRL+ALT+SPACE	快速导入任意类
    2	CTRL+SHIFT+ENTER	代码补全
    3	SHIFT+F1	查看外部文档
    4	CTRL+Q	快速查找文档
    5	CTRL+P	参数信息（在方法中调用的参数）
    6	CTRL+MOUSEOVERCODE	基本信息
    7	CTRL+F1	显示错误或警告的描述
    8	CTRL+INSERT	生成代码
    9	CTRL+O	重载方法
    10	CTRL+ALT+T	包裹代码
    11	CTRL+/	单行注释
    12	CTRL+SHIFT+/	块注释
    13	CTRL+W	逐步选择代码（块）
    14	CTRL+SHIFT+W	逐步取消选择代码（块）
    15	CTRL+SHIFT+[	从当前位置选择到代码块的开始
    16	CTRL+SHIFT+]	从当前位置选择到代码块的结束
    17	ALT+ENTER	代码快速修正
    18	CTRL+ALT+L	代码格式标准化
    19	CTRL+ALT+O	最佳化导入
    20	CTRL+ALT+I	自动缩进
    21	TAB	代码向后缩进
    23	SHIFT+TAB	代码向前取消缩进
    24	CTRL+SHIFT+V	历史复制粘贴表
    25	CTRL+D	复制当前代码行/块
    26	CTRL+Y	删除当前代码行/块
    27	CTRL+SHIFT+J	代码连接为一行
    28	SHIFT+ENTER	开启新一行
    28	CTRL+SHIFT+U	字母大写
    29	CTRL+DELETE	向后逐渐删除
    30	CTRL+BACKSPACE	向前逐渐删除
    31	CTRL+NUMPAD+/-	代码块展开/折叠
    32	CTRL+SHIFT+NUMPAD+	所有代码块展开叠
    33	CTRL+SHIFT+NUMPAD-	所有代码块折叠
    34	CTRL+F4	关闭活动编辑窗口
    
    
        二、搜索/替换快捷键
     
    1	CTRL+F	查找
    2	F3	查找下一个
    3	SHIFT+F3	查找上一个
    4	CTRL+R	替换
    5	CTRL+SHIFT+F	指定路径下查找
    6	CTRL+SHIFT+R	指定路径下替换
    
    
        三、代码运行快捷键
     
    1	ALT+SHIFT+F10	选择程序文件并运行代码
    2	ALT+SHIFT+F9	选择程序文件并调试代码
    3	SHIFT+F10	运行代码
    4	SHIFT+F9	调试代码
    5	CTRL+SHIFT+F10	运行当前编辑区的程序文件
    
    
        四、代码调试快捷键
    
    1	F8	单步
    2	F7	单步（无函数时同F8）
    3	SHIFT+F8	单步跳出
    4	ALT+F9	运行到光标所在位置处
    5	ALT+F8	测试语句
    6	F9	重新运行程序
    7	CTRL+F8	切换断点
    8	CTRL+F8	查看断点
    
    
        五、应用搜索快捷键
     
    1	ALT+F7	查找应用
    2	CTRL+F7	在文件中查找应用
    3	CTRL+SHIFT+F7	在文件中高亮应用
    4	CTRL+ALT+F7	显示应用
    
    
        六、代码重构快捷键
     
    1	F5	复制文件
    2	F6	移动文件
    3	SHIFT+F6	重命名
    4	ALT+DELETE	安全删除
    5	CTRL+F6	改变函数形式参数
    6	CTRL+ALT+M	将代码提取为函数
    7	CTRL+ALT+V	将代码提取为变量
    8	CTRL+ALT+C	将代码提取为常数
    9	CTRL+ALT+F	将代码提取为字段
    10	CTRL+ALT+P	将代码提取为参数
    
    
        七、动态模块快捷键
     
    1	CTRL+ALT+J	使用动态模板包裹
    2	CTRL+J	插入动态模板
    
    
        八、导航快捷键
    
    1	CTRL+N	进入类
    2	CTRL+SHIFT+N	进入文件
    3	CTRL+ALT+SHIFT+N	进入符号
    4	CTRL+←←	进入上一个编辑位置
    5	CTRL+→→	进入下一个编辑位置
    6	CTRL+→→	进入下一个编辑位置
    7	SHIFT+ESC	隐藏活动/最后活动的窗口
    8	CTRL+SHIFT+F4	关闭活动的运行/消息/查找等窗口
    9	CTRL+G	显示光标所在行与列
    10	CTRL+E	弹出最近打开的文件
    11	CTRL+ALT+←/→←/→	向前/向后导航
    12	CTRL+SHIFT+BACKSPACE	导航到最后编辑的位置
    13	CTRL+B	跳转到声明部分
    14	CTRL+CLICK(鼠标左键)	跳转到声明部分
    15	CTRL+ALT+B	跳转到代码实施部分
    16	CTRL+SHIFT+I	打开快速定义查找
    16	CTRL+SHIFT+B	跳转到类型说明
    17	CTRL+U	跳转超类/方法
    18	CTRL+↑↑	跳转到上一个方法
    19	CTRL+↓↓	跳转到下一个方法
    20	CTRL+[	跳转到代码块的开头
    21	CTRL+]	跳转到代码块的结尾
    22	CTRL+F12	弹出文件结构
    23	CTRL+H	弹出类层次结构
    24	CTRL+SHIFT+H	弹出方法层次结构
    25	CTRL+ALT+H	弹出调用层次结构
    26	F2/SHIFT+F2	下一个/上一个错误
    27	F4	查看源代码
    28	ALT+HOME	显示导航栏
    29	F2/SHIFT+F2	下一个/上一个错误
    30	F11	增加书签
    31	CTRL+F11	增加数字/字母书签
    32	CTRL+SHIFT+[1-9]	增加数字书签
    33	SHIFT+F11	显示书签
    
    
        九、通用快捷键
   
    1	ALT+[0-9]	打开相应的工具窗口
    2	CTRL+ALT+Y	同步
    3	CTRL+SHIFT+F12	最大化编辑器
    4	ALT+SHIFT+F	添加到收藏夹
    5	ALT+SHIFT+I	使用当前配置文件检查当前文件
    6	CTRL+ALT+S	快速出现设置对话框
    7	CTRL+SHIFT+A	查找并调试编辑器的功能
    8	ALT+TAB	在选项卡和工具窗口之间切换
    
'''
