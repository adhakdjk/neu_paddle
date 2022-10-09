# 本周总结
## 学习进度/本周学习
* python：部分文件的读取操作，循环的写法，一部分函数的调用
* C++ ：能打学过的数学知识：矩阵乘法，逆矩阵求法，adj矩阵，没把C++忘光
* 深度学习：能够实现精度误差的求法，并能实现简单的数据清洗，数学模型初步了解点皮毛，训练集划分，numpy与pandas运用更加熟练~还能画图~
* 实践：一两个短代码，放在code里了

## 问题总结
* 多，特别多，挑几个出来说一说。
### 1.关于二维数组取段以及行列的问题（单独的知识点，难以理解但很重要）
* python中利用numpy对数组进行分段---->提取每一维的部分
#### dataframe 的用法
* 主要是利用数组进行创建
先建立数组：
```
data=np.random.randn(6,4)#创建一个6行4列的数组
df=DataFrame(data,columns=list('ABCD'),index=[1,2,'a','b','EVA','EVA_1'])

```
result:
>>[![BMP.png](https://i.postimg.cc/D00Zykzp/BMP.png)](https://postimg.cc/0Kgxc4D7)
#### [ : ] 与 [ :  : ]的用法
* [起始位置 :  : 跳跃的次数]  ||  [起始位置 : : -1] ( 反转输出 ) --->对于二维数组都可以
* [起始位置 ： 最后一个数+1]
* 对于表格数据的话：DataFrame 就不行，当然，具体问题具体分析

### 2.关于iloc与loc的问题
* iloc 指的是以行数为前提，而不以索引为前提进行查找
* loc 则是以索引为前提的查找，就是直接data.loc[ 索引，无论数字字符 ]

### 3.关于CSV文件转数组问题
* 有两种转法
* 1.
```
import numpy as np
mydata = np.loadtxt(open("example.csv","rb"),delimiter=",",skiprows=0) 
```
* 2.
```
data=np.array(mydata)  ---->简单又暴力的美学
```
### 4.关于python不能输出中文问题
这个就是纯粹的知识问题，在CSDN上搜了一下，若它是自带的utf-8无法解码，就在文件的开头加上一个,改为gbk解码
```
#coding gbk 
```

### 5.（技术）python中缺失numpy库
* 错误日志为
```
ModuleNotFoundError: No module named 'numpy'
```
* 存在问题：可能python库中没有numpy（未知的问题）
* 解决方案：
1. 打开电脑中的python文件,一般目录为
```
C:\Users\user\AppData\Local\Programs\Python
```
2. 打开Scripts，按住shift+鼠标右键，点击在此处打开powershell窗口
3. pip install numpy 回车即可
4. 就可以用啦。。。
## 感悟：
本周的学习有好有坏：  
#### 好处
养成了不懂的在CSDN上搜答案的习惯，CSDN上的东西真的很多，还有各种新奇好玩的东西，就是~一些大佬排版不怎么样影响阅读。。~也学会了零零散散的一些模型，也靠自己解决了许多难题，很有成就感
#### 不足之处
学到的东西是很多，但他们都太过于零散，太容易忘记，学习的进度也一直卡在同一个地方，解决问题的速度还不够快，以后就在周末总结中总结一下知识点，看看前面的总结，找找不足，学东西不能得过且过，要有刨根问底的精神，深度学习还需要跟进。。书也是要啃的

![text](https://i0.hdslb.com/bfs/article/124aa9a9f688cad6cef2edbe8341a9f30c5b4376.jpg@942w_531h_progressive.webp)
## 成就
无




