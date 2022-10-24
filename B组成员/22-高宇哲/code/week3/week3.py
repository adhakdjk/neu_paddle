"""def student_name_and_age(name, age='不愿透露'):
    print('姓名：%s 年龄 %s' %(name, age))
name=input('name:')
age=input('age=')"""


"""def student_name_and_age(name, age='不愿透露'):
    print('姓名：%s 年龄 %s' %(name, age))
name=input('name?')
age=input('age?')
student_name_and_age(name,age)"""

""""
def names(*name):
    for name in name:
        print("name:",name)
name=('1','2','3')
names(*name)
"""

"""def person_info(name,age,**kw):
    print(f'name:{name},age:{age}')
    if 'city' in kw:
        print('city:',kw['city'])

person_info('hhh','19',weather='fine',city='sx')"""

"""si={'city':'sx','weather':'fine'}
person_info('hhh',18,**si)"""

"""def student_info(name, age, **kw):
    print(f'我的名字叫：{name},年龄：{age},其它信息：{kw}')
    if 'city' in kw:
        print('来自：', kw['city'])
student_info('张三', 18, height=180, city='北京')"""

"""def print_person_info(name, age, *,height, weight):
    print('我的名字叫：', name, '年龄：', age,'身高', height, '体重', weight)
print_person_info("hhh", 12, height=188, weight=75)"""

"""print((lambda arg1,arg2:arg1+arg2)(1,2)) #匿名函数
add=lambda arg1,arg2:arg1+arg2
print(add(1,2))"""

"""def count():
    global fs
    fs = []
    for i in range(1, 4):
        def f():
            # print(id(i))
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())"""

def print_working(func):
    def wrapper():
        print(f'{func.__name__} is working...')
        func()
    return wrapper

def worker1():
    print('我是一个勤劳的工作者！')
def worker2():
    print('我是一个勤劳的工作者！')
def worker3():
    print('我是一个勤劳的工作者！')

worker1 = print_working(worker1)
worker1()
worker2= print_working(worker2)
worker2()