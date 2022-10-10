
# 本周总结

## 本周学习内容
- 学习使用ai studio
- 学习python基础

## 知识点总结（AI STUDIO）
### 创建项目

### 单元格（cell)
两种模式：编辑模式(绿)和命令模式(蓝)
快捷键（菜单中有提示）

## 知识点总结（python基础）
### 输入输出
输入：input("XXX")  //XXX为输入时提醒的内容

输出：print("XXX")  //XXX为输出内容

### 注释
- 单行：#
- 多行：  """
        XXXX
        XXXX
        XXXX
        """

### python识别代码段：
缩进或空格，但是必须统一

### 基本数据类型
#### 运算符
+    -   *   
/(除法)   //(向下整除)   %(取余数)   **(幂运算)

#### 数据类型
python无需声明

#### 浮点数计算精度控制
round(a+b,c)  c为精度位数

#### 运算优先顺序（如图）
tip:使用小括号

#### 字符串
使用" " 或 ' '
字符串中有引号：使用 " " 套 ' ' 或用 \" 转译

#### 布尔值
注意大小写 True or False

#### 空值
none

#### 运算规则
num+=2 == num=num+2     //与C++不同，python无 i++

#### 起名法则
1.第一个字符非数字
2.非保留字
3.可选下划线/数字/字母

#### 数据类型转化
eg.   str(4)    float('0.6')   //不可跳步转化如int('0.6')

### 组合数据类型

#### list
list:有序集合可增删 使用中括号 [ ]
- eg. list1=['phy',123,1.23]
- 访问元素：list1[2]
- 新增元素：list1.append("abc")
- 弹出：list1.pop(X)   //list在pop后会少这个元素，tuple则不会
- 翻转元素：list1.reverse()

#### tuple
tuple:一旦初始化不可更改  使用小括号 ( )
- tuple1=(1,2,3,4,5)

#### dict 
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度  使用大括号 { }
- dict：{"key":"value"}
- 不同key：value用逗号,隔开

- 访问：dict["key"]
- 修改：dict["key"]=XX

#### set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。 使用大括号 { }

### 判断
#### 基本语句
if xxx:
- else if xxx:
- else:

#### 判断语句
- print(1==2)  //判断是否相等
- print(1!=2)  //判断是否相等
- print(1>2)  //判断是否相等
- print(1<2)  //判断是否相等
- print(1>=2)  //判断是否相等
- print(1<=2)  //判断是否相等

#### 逻辑运算符
 not>and>or

### 循环
#### while
- while 条件 ：
- xxxxx
- xxxxx

#### for
- for i in range(x) :
- for x in list1 :
- for letter in "hhhhh" :

#### break
跳出循环

#### continue
继续循环，跳过本轮

#### pass
占位，先让程序跑起来


## 问题总结

### 书写程序时，出现：输入法在英文状态下仍打出全角符号

- 解决方案
状态栏右侧 英-右键-全半角-选择半角 

### 访问list中的元素
- AI STUDIO(notebook) 可以直接 list[3] 执行
- VS 必须print(list[3])

## 感悟(选填)

- 自己写起来还是有很多问题的，听课后要多实践

