
# 本周总结

## 本周学习

1，python安装

2，VScode安装

3，在VScode中配置python

4，Git安装

5，利用 SSH 完成 Git 与 GitHub 的绑定

## 知识点总结

### git常用命令

- git安装后-指定名称和邮箱

  ```
  $ git config --global user.name "Your Name"
   
  $ git config --global user.email "email@example.com"
  ```

- 创建版本库

  ```
  $ mkdir oldgeek-learn	//创建
  $ cd oldgeek-learn	//使用
  $ pwd	//查看当前目录
  $ git init	//初始化，生成.git文件(若该文件隐藏，则使用ls -ah)
  ```

- 版本控制

  ```
  $ git log	//查看提交历史记录，从最近到最远，可以看到3次
  $ git log --pretty=oneline	//加参，简洁查看
  $ git reflog	//查看每一次修改历史
  $ cat test.txt	//查看文件内容
  $ git status	//查看工作区中文件当前状态
  $ git reset --hard HEAD^（HEAD~100）（commit id）	//回退版本
  $ git checkout -- test.txt	//丢弃工作区的修改，即撤销修改
  $ git reset HEAD test.txt	//丢弃暂存区的修改（若已提交，则回退）
  ```

## 问题总结

### 在vscode中配置python时，出现：vs版本与教程所用版本不同，配置错误

- 解决方案

按ctrl+shift+P，在弹出的命令面板里输入
 python:select interpreter
选择那个选择解释器的选项 然后就会出现python解释器的选择列表，已经添加的都会在这里显示。新安装的python解释器需要通过图中的 ‘’输入解释器路径’‘ 进行添加。

- 参考资料
python安装vscode配置，入门记录 https://blog.csdn.net/qq_26288221/article/details/123134675?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166333777216782427495041%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166333777216782427495041&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-123134675-null-null.142^v47^new_blog_pos_by_title,201^v3^add_ask&utm_term=VSCOD%E9%85%8D%E7%BD%AEpython&spm=1018.2226.3001.4187

### 在git中配置user.name和user.email,否则云仓库提交时会报错
-解决方案

git bash中输入
  $ git config --global user.name "Your Name"
   
  $ git config --global user.email "email@example.com"

## 感悟(选填)
-认真听讲很重要 
-百度也可解千愁

## 成果展示
预备周.png
