# Git的安装和初始化配置

## 一、安装

1. 去[git官网](https://git-scm.com/)进行下载并安装
2. 验证安装：在终端输入`git -v`命令


​	看到版本信息说明安装成功

------

## 二、Git的使用方式

### 1.命令行

最基本、最常用，在终端中使用git命令来操作Git

Git的所有命令都以`git`开头

### 2.图形化界面（GUI）

通过一些专用的图形化工具使用Git

### 3.IDE插件/扩展

在IDE中通过扩展或者插件来使用Git（VSCode默认集成了源码管理器）

------

# 三、初始化配置

1.使用`git config`命令配置邮箱和用户名，为了识别出是谁提交的内容

**配置用户名：**

```shell
git config --global user.name "Binfinity"
```

**配置邮箱：**

```shell
git config --global user.email 2870639124@qq.com
```

**保存用户名和密码**（这样不用每次都输入）**：**

```shell
git config --global credential.helper store
```

**查看配置信息：**

```shell
git config --global --list
```



|     参数      |           表示           |
| :-----------: | :----------------------: |
| 省略（Local） | 本地配置，只对本仓库有效 |
|   --global    |  全局配置，所有仓库生效  |
|   --system    | 系统配置，对所有用户生效 |

