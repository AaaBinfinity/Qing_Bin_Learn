# Answers to questions!!!

------

### 问题：

`push` 时出现错误：

```shell
Please make sure you have the correct access rights and the repository exists 
```

请确保您具有正确的访问权限并且存储库存在

### 解决：

公钥出问题了,需要删除.ssh下文件,然后重设置用户名和邮箱再重新生成ssh公钥即可解决

1. 删除.ssh下所有所有文件，Windows路径：`C:\Users\****\.ssh`

2. 输入命令生成密钥：

   ```shell
   ssh-keygen -t rsa -C "Email@email.com"
   ```

3. 再次配置Github密钥