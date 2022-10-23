def student_name(name):
    # "打印学生的名字"
    print('姓名：', name)
    return {'姓名':name} # 返回字典类型

rst = student_name('Alice')
print(rst)

def student_name_and_age():
    name = input("请输入姓名\n")
    age = input("请输入年龄\n")
    print(f'姓名:{name} 年龄:{age}')
    return name,age #相当于元组

 # rst1 = student_name_and_age()
# name, age = student_name_and_age()

##函数的嵌套调用
def worker(s): #工人
    rst = 10/float(s)
    return rst

def group_leader(s):  #小组长
    rst = worker(s)*2
    return rst
def CTO(s):
    return group_leader(s)

print(CTO('4'))

# 参数传递

# 可变参数 加个*
def all_students_name(*names):
    for name in names:
        print('姓名:',name)

# all_students_name('张三','李四','王五')

# 关键字参数 **表示关键字参数
# 参数定义的顺序必须是，必选参数，默认，可变，命名，关键字
# 命名与关键同用的时候命名的*必须省略，所以city其实是命名关键字参数
def student_info(name,age=18,*books,**kw):
    print(f'我的名字叫:{name},年龄:{age},其他信息:{kw}')
    if'city'in kw:
        print(name,'来自',kw['city'])
    for book in books:
        print('我有',book,'书')
    print(type(name))
    print(type(kw))

student_info('张三',18,height=180,city='北京')

print("\n----关键字参数用例----")
def score_info(name,**kw):
    if '语文成绩' in kw:
        print(name,'语文成绩为',kw['语文成绩'])
    if '数学成绩' in kw:
        print(name,'数学成绩为',kw['数学成绩'])

def person_info(name,age,**kw):
    print(name,age)
    score_info(name,**kw)

score_cfg = {'语文成绩':95,'数学成绩':100,'英语成绩':100}
person_info('zhangsan',18,**score_cfg)
print("---------------\n")

# 命名关键字参数 加个,*,  *单独占个位，后面都是命名。。。

def print_person_info(name, age, *, height, weight):
    print('我的名字叫：', name, '年龄：', age,'身高', height, '体重', weight)

print_person_info('张三', 18, height=180, weight=75)
# 必须要写height=啥

