# # 切片语法
# name = 'molly'
# print(name[1])
# print(name[-4])
# print(name[1:4])
# print(name[::1])  # name[:] 也可以复制整个序列
#
# string = 'Hello world!'
# print(string[2])
# print(string[2:7])
# print(string[3:])
# print(string[8:2:-1]) # 字符串要是end标明了不会打印end的元素
# print("\n")
#
# for s in string:
#     print(s)
# print("\n")
#
# # 如果字符串以‘p'结尾，则打印
# list_string = ['apple', 'banana_p', 'orange', 'cherry_p']
# for fruit in list_string:
#     if fruit[-1] == 'p':
#         print(fruit)
#
# # 如果字符串已pr结尾，则打印 三击选择一行
# list_string1 = ['apple', 'banana_pr', 'orange', 'cherry_pr']
# for fruit1 in list_string1:
#   if fruit1.endswith('pr'):
#      print(fruit1)



print("\n-----字符串常见函数-------\n")
# count计数功能  显示自定字符在字符串中的个数
my_string = 'hellol_wolrld'
print(my_string.count('ol'))
print("\n")
# help(my_string.count)

# find查找功能，返回从左第一个指定字符的索引，找不到返回-1
# index 查找， 返回从左第一个指定字符的索引，找不到报错
print("index和find查找函数")
my_string = 'hello_world'
print(my_string.find('o'))
print(my_string.index('o'))
# print(my_string.index('a'))
print(my_string.find('a'))
print("\n")

# 字符串的拆分
my_string = 'hello_world'
my1 = my_string.split("_")
print(my1[1])

# 字符串的替换 从左到右替换指定的元素，可以指定替换的个数
my_string = 'hello_world'
my = my_string.replace('_', ' ')
my1 = my_string.upper();  # 全部改为大写   lower全部改为小写
my2 = my_string.strip('h')   # 默认去除两边的空格，换行符之类
print(my)
print(my1)
print(my2)
my3 = my_string.capitalize()
print(my3)

print("\n-----字符串的格式化输出-----")
accuracy = 80/123
print('模型正确率是%s' % accuracy)
print('模型正确率是%.2f' % accuracy)
print('模型正确率是', accuracy)

name = 'Molly'
hight = 170.4
score_math = 95
score_english = 89
print("大家好，我叫%s，我的身高是%dcm,数学成绩是%.2f分，英语成绩%d分" % (name,hight,score_math,score_english))


"""
指定了 :s ，则只能传字符串值，如果传其他类型值不会自动转换
当你不指定类型时，你传任何类型都能成功，如无特殊必要，可以不用指定类型
"""

print('大家好！我叫{}，我的身高是{:d} cm, 数学成绩{:.2f}分,英语成绩{}分'.format(name, int(hight), score_math, score_english))

'Hello, {0}, 成绩提升了{1:.1f}分，百分比为 {2:.1f}%'\
    .format('小明', 6, 17.523)

'Hello, {name:}, 成绩提升了{score:.1f}分，百分比为 {percent:.1f}%'\
    .format(name='小明',
            score=6,
            percent = 17.523)

list = ['a','b','c']
print(list[2])

print("\n---format用法-----\n")
print("我叫{}，今年{:.2f}岁。".format("小蜜",18))
# 我叫小蜜,今年18岁。
# 花括号的个数决定了，参数的个数。但是花括号的个数可以少于参数。
# print("我喜欢{}和{}"format("乒乓球","羽毛球","敲代码"))
# 我喜欢乒乓球和羽毛球。
"""
花括号多于参数的个数，则会报错。
"""

# 2.通过数字索引传入参数
print(("名字{0},家住{1}").format("橙留香","水果村"))
#带数字的替换1字段可以重复

print("我爱{0}。\n他爱{1}。\n{0}爱{1}".format("灰太狼", "红太狼"))
"""
我爱灰太狼
他爱红太狼
灰太狼爱红太狼
"""

"""
数字形式的简单字段名相当于把字段当成一个序列形式。通过索引的形式进行一一取值
"""
print("小明喜欢{1},{2}和{0}".foramt("海绵宝宝", "机器猫", "海贼王", "火影忍者","龙珠"))
#小明喜欢机器猫，海贼王，和海绵宝宝

# 利用关键字传递
print("今年我{age}岁，我在读{college}".format(age=18, college="大学"))
