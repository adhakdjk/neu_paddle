# 本周总结  

## 本周学习  

在"飞桨领航团AI达人养成营"学python课节2  

## 知识点总结  

### 课节2  

#### 1、学习字符串的索引和切片  
#### 2、了解字符串常用函数  
新知识：  
1).count()  
2).find() .index()  
3)巧用条件判断 in 
4).split()  
5).replace()  
6)字符串的三种格式化输出  
- %
- {} + .format()
- f-string  

#### 3、list常用函数  
新知识：
1).insert()
2).extend()

#### 4、  
列表生成式  
[表达式 for 变量 in 列表]  

或者   

[表达式 for 变量 in 列表 if 条件]  

元组生成式（生成器generator）  

yield浅析：  
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()  
（在 for 循环中会自动调用 next()）  
才开始执行。  

虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处:  
把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。

如何判断一个函数是否是一个特殊的 generator 函数？  
可以利用 isgeneratorfunction 判断：


```python  
from inspect import isgeneratorfunction  

isgeneratorfunction(fab) 
True  
```

#### 5、异常与错误处理
1.  
```python
try:
    <语句>        #运行语句

except <名字>:
    <语句>        #如果在try语句里引发了<名字>异常

except <名字>, <数据>:
    <语句>        #如果引发了<名字>异常，获得附加的数据

else:
    <语句>        #如果没有异常发生
    
finally:
    <语句>        #有没有异常都会执行
```

2.assert语句

<br/>
见 课节2.ipynb


## 问题总结  

错误日志


解决方案


参考资料


## 感悟(选填)  
1、不知道函数的用法就百度  
2、感觉python复健地有点慢，先去康康深度学习

## 成果展示  

TO BE CONTINUED