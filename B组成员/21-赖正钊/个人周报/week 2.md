# 本周总结  

## 本周学习  

在"飞桨领航团AI达人养成营"学python  
 

## 知识点总结  

### 课节1  

#### 课节1.1 [项目]Notebook基础操作  

Notebook中使用Shell命令  
<br/>  

通过在Shell命令前 添加 ! (感叹号), 就可以执行部分Shell命令.  

eg:  
    
    # 查看当前挂载的数据集目录
    !ls /home/aistudio/data/  
<br/>  
    
    #显示当前路径
    !pwd  
<br/>

(其他的感觉跟jupyternotebook差不多)  
<br/>  

#### 课节1.2 [文档]Python计算机基础  

1、编程语言  
2、计算机基本组成  
控制器，运算器，存储器，输入设备，输出设备  
3、计算机系统  
计算机硬件  计算机软件  
4、进制(略)  
5、浮点数  
32位单精度浮点数：1位符号位+8位指数+23位小数  
64位双精度浮点数：1位符号位+11位指数+52位小数  
! 在Python中不建议直接将两个浮点数进行大小比较 !  
<br/>  

#### 课节1.3 [项目]课节1: Python环境搭配搭建入门教程  

1、早就已经装好anaconda全家桶哩  
2、语法基础  
1 / 2       除法  
1 // 2      整除  
1 % 2       取余  
2 ** 2      幂运算   


字符串是以单引号'或双引号"括起来的任意文本  
 
True False  布尔值可以用and、or和not运算  
 
None    空值是Python里一个特殊的值，用None表示  
None不能理解为0，因为0是有意义的，而None是一个特殊的空值  
<br/>  

组合数据类型  
<br/>  
列表    list（[]括号）  

    list1 = [1, 2, 3, 4, 5 ]  
    list2 = ["a", "b", "c", "d","e","f"]  
    list3 = ['physics', 'chemistry', 1997, 2000]  

reverse()函数 把list中所有元素翻转  
<br/>  

元组    tuple（()括号）  
与list的区别：tuple一旦初始化就不能修改  

    tuple1 = (1, 2, 3, 4, 5 )  
    tuple2 = ("a", "b", "c", "d","e","f")  
    tuple3 = ('physics', 'chemistry', 1997, 2000)
<br/>  

字典    dict（{}括号）    用“键-值(key-value)”存储  

    word = {'apple':'苹果','banana':'香蕉'}  
    scores = {'小张':100, '小李':80}  
    grad = {4:'很好',3: '好',2:'中',1:'差',0:'很差'}  
<br/>  

集合    set（{}括号）  
set和dict类似，也是一组key的集合，但不存储value。  
由于key不能重复，所以，在set中，没有重复的key。  

    s = {1, 1, 2, 3, 4}  
<br/>  

for循环  

    fruits = ['banana', 'apple',  'mango']  
    for fruit in fruits:        # 第一个实例  
    print( '当前水果 :', fruit)
    
    for letter in 'Python':     # 第二个实例  
    print( '当前字母 :', letter)  







  见  课节1.ipynb


## 问题总结  

错误日志


解决方案


参考资料


## 感悟(选填)  


## 成果展示  

TO BE CONTINUED