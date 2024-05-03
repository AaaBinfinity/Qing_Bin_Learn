# SSH配置和克隆仓库

如何使用GitHub来管理代码

要使用SSH协议来克隆远程仓库，首先需要将密钥添加到GitHub上

在文件夹`.ssh`中打开终端

```shell
ssh-keygen -t rsa -b 4096
```

若是第一次使用该命令，直接回车就可以，会在`.ssh`文件夹下添加密钥

将公钥的内容复制到GitHub上即可

使用克隆命令将本地的远程仓库克隆到本地

```shell
git clone <url>
```

**注意：**在本地仓库修改的文件不会同步到GitHub的远程仓库，因为Git是一个分布式的版本控制系统，每个仓库是相互独立的

### 如何同步？

将本地仓库的修改推送给远程仓库

```shell
git push <remote> <branch>
```

把远程仓库的修改拉取到本地仓库

```shell
git pull <remote>
```

