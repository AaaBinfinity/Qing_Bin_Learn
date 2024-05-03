# 使用`git diff`查看差异

`git diff`命令可以用来查看文件再工作区、暂存区、版本库之间的差异

还可以查看文件在不同版本之间的差异，或者文件在两个分支之间的差异

更多的是使用一些图形化的工具

------

`git diff`命令的默认参数是比较工作区和暂存区之间的差异内容，会显示发生更改的文件以及更高的详细信息

比较工作区和版本库之间的差异

```shell
git diff HEAD
```

比较暂存区和版本库之间的差异

```shell
git diff --cached
```

比较两个特定版本之间的差异，在后面加上需要比较的两个版本的提交ID

```shell
git diff <ID1> <ID2>
```

还和一使用`HEAD`来表示当前分支的最新提交，`HEAD`指向分支的最新提交节点

```shell
git diff <ID1> HEAD
```

比较当前版本和上一个版本之间的差异，`HEAD~`或者`HEAD^`可以表示上一个版本

```shell
git diff HEAD~ HEAD
```

```shell
git diff HEAD^ HEAD
```

`HEAD~`后边跟上数字可以表示`HEAD`之前的几个版本，例如，`HEAD~2`表示`HEAD`之前的两个版本

`git diff`命令后面也可以加上文件名，表示只查看这个文件的差异内容

```shell
git diff HEAD^ HEAD <file>
```

`git diff`命令还可查看两个分支之间的差异
