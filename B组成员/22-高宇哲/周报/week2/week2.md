# 本周总结

## 本周学习

- 课节2: Python编程基础

## 知识点总结
### 上节课回顾
- range（3，5）
 左闭右开 包含3，4

### 字符串进阶

#### 字符串索引、切片
- 切片的语法：[起始:结束:步长] 字符串[start: end: step] 这三个参数都有默认值，默认截取方向是从左往右的 start:默认值为0，从0开始； end : 默认值未字符串结尾元素； step : 默认值为1；start在end左边

 如果切片步长是负值，截取方向则是从右往左的，start从-1开始，start在end右边


#### 字符串常用函数
- count计数功能
 显示自定字符在字符串当中的个数
 count 是不重叠查找 "aaaaaa"中有3个aa

- find 查找功能 
 返回从左第一个指定字符索引 找不到则返回-1

- index 查找
 返回从左第一个指定字符的索引，找不到报错


- 关键字：in
 返回True False

- split 字符串的拆分
按照指定的内容进行分割
分割后元素组成新的tuple

- replace 字符串的替换
 从左到右替换指定的元素，可以指定替换的个数，默认全部替换
 精确替换：a.replace("a","b".upper(),3) 只替换3个a

- strip 字符串标准化
 只能去除 首尾 的空格、换行符之类的，去除内容可以指定
 
- 字符串的变形
 a.lower() 小写
 a.upper() 大写
 a.capitalize() 首字母大写

#### 字符串的格式化输出
- % 
 具体内容见图 %的格式与描述.png
 举例：
 accuracy = 80/123
 print('老板！我的模型正确率是%.2f!' % accuracy)

- format
 用{}占位
 指定了 :s ，则只能传字符串值，如果传其他类型值不会自动转换
 当你不指定类型时，你传任何类型都能成功，如无特殊必要，可以不用指定类型
 eg.
 'Hello, {name:}, 成绩提升了{score:.1f}分，百分比为 {percent:.1f}%' .format(name='小明',  score=6, percent = 17.523)

- 一种可读性更好的方法 f-string
 print(f"I am {name.capitalize()}.Height is {height:.3f}cm")

### list 进阶
#### list索引，切片
list1[2]
list1[2:5]

#### list 常用函数
- 添加新元素
 list1.append("5")在末尾增加 5  list1.insert(2,"5")在第三个后面增加 5   list1.extend(list2) 把list1变为list1与list2之和（即合并1和2）

- 计数和查找
list1 = ['a','b','a','d','a','f']
print(list1.count('a')) 查找a的个数
print(list1.index('a')) 查找a的位置

- 删除元素
pop(x) x是list中的第x+1项
remove(x) x是list中的元素

### 列表生成式-中括号
- 列表每一项加一
[n+1 for n in list1]
- 1-10之间所有数的平方 
[(n+1)**2 for n in range(10)]
- 1-10之间所有数的平方 构成的字符串列表
[str((n+1)**2) for n in range(10)]

- list1 = ['a','b','a','d','a','f']
['app_%s'%n for n in list1]

- list1 = ['a','b','a','d','a','f']
[f'app_{n}' for n in list1]

- 列表中的每一个偶数项[过滤]
 [n for n in range(30) if n%2==0]

- 小练习 在list_A 但是不在list_B中
list_A = [1,3,6,7,32,65,12]
list_B = [2,6,3,5,12]
[i for i in list_A not in list_B]

### 生成器-小括号
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#### 具体应用
- 生成器.py

## 问题总结
- 列表生成式执行后不会改变原列表