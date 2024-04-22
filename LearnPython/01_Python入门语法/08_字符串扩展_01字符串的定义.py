# 字符串的三种定义法

# 1.单引号定义法
name = 'binfinity'
print(name)
# 2.双引号定义法
name = "binfinity"
print(name)
# 三引号定义法
name = """Binfinity"""
print(name)

# 字符串的引号嵌套

# 嵌套的引号不能跟定义用的引号相同
name = '"binfinity"'        #定义的效用被单引号占用了
print(name)
name = "'binfinity' "       #定义的效用被单引号占用了
print(name)
# 必须相同的话可以使用（\）来将被嵌套的引号解除效用，变成普通字符
name = "\"binfinity\""
print(name)



