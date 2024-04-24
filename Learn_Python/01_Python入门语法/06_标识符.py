'''
标识符 命名，只允许出现：
1.中文    (不推荐)
2.英文    （可以区分大小写）
        不可使用关键字：
            例如False、True、for等等(同样大小写敏感)
3.数字    （不可以用在开头）
4.下划线“_”
'''""""""""

# 内容限定：
Binfinity = 222
binfinity = 123  # 大小写敏感（python的变量定义中要区分大小写）
name_my = "CaoBin"
李绮卿 = 250
bin23 = 157
print(Binfinity)
print(binfinity)
print(name_my)
print(李绮卿)
print(bin23)
# 23shjcido     不可以以数字开头
# class = 12    不可以使用关键字
Class = 123  # 但是可以打写（大小写敏感，只要大小写不完全一样就可以使用）
