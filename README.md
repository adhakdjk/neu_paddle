# neu_paddle
本仓库用于百度飞桨领航团 技术组成员培训。

# Paddle

## NEUQ百度飞桨领航团周报收集

> 本项目用于东北大学百度飞桨领航团培训，未加入仓库协作者请联系领航团团长。
> 
> This project is for the Northeastern University Baidu Paddle Pilot Group training, please contact the Leaders for those who are not collaborators.



---



### 周报要求

新建一个以年级-姓名命名的文件夹(For example: 21-宋梓瑞) ，使用Markdown格式编写，上传至相应文件夹中，命名为：week0-宋梓瑞  
week0代表预备周，正式周以week1开始顺延。

个人文件夹要求必须包括 code文件夹 和个人周报文件夹。有能力者可以设置每日总结文件夹。
c


#### 具体格式要求：



# 本周总结

## 本周学习


- 安装VSCODE并配置python环境
- 安装Git并连接Github
- 学习python基础

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

### 安装Java时，出现：XXXXXXX

- 错误日志

  ```
  XXXX
  ```

- 解决方案

  - XXX
  - XXX
  - XXX

- 参考资料

  - [XXX](XXX)

## 感悟(选填)

- XX
- XX

## 成果展示
> 内容包括: 个人搭建的博客链接 或CSDN原创文章链接。
