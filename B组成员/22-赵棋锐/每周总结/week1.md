# 本周总结
## 本周学习/知识点总结
* 了解何为机器学习，深度学习，向大佬请教了学习AI的方法。。。
* 了解paddle notebook 的基本用法
* 以下是我的学习计划（详见9.26.md）的学习进度
### python
* 完成[Python从小白到精通]的1~3章（共6章）
#### python 的具体知识点
* python 的基本语法
* python 的基本的文本编辑与字母统计（破译密码）
1.读取文件(提取文件中的字符)  
```
f=open('/home/aistudio/work/novel1')
test=f.read()
print(test)
可以对test进行任意操作
```
2.打开csv文件  
```
import pandas as pd(学过C++所以我猜想其相当于一个结构体（EVA a）)
f=pd.read_csv('wenjianmulu')
f
```
3.统计字符的多少
```
1.把所有的字符小化
text=text.lower()
2.便历所有的字符
counter={}
for i in test:
    if i not in counter: counter[i]=1
    else : counter[i]+=1
```
3.数据清洗  
* 使用数据清洗前需要导入一个库
```
import pandas as pd
```
* 然后就可以使用操作了
##### 打开csv文件
```
test=pd.read_csv('目录')
test
```
##### 
4
### 机器学习的具体知识点
* 完成[李宏毅机器学习]的机器学习的基本概念
* alphago所运用的技术是
先是supervised Learning（例如老师教学生什么是对，什么是错）  
再是reinforcement Learning (学会自己判断什么是对，什么是错)  
此外还有structure Learning  
#### 用gradient Desecent 找参数
* 提前找到 local optimal 的解决方案：
由于local optimal的寻找是由积分（斜率判断寻找的 ）他可能提前找到。。。。。。
>>>[![BMP.png](https://i.postimg.cc/7hSYQ9r3/BMP.png)](https://postimg.cc/gLkWxvJj)
* 解决方案--->linear regression
* 完成[深度学习-deep-learning]的线性代数的部分知识点
## 错误日志
* Git 无法将文件同步到GitHub上
