
string = 'Hello world!'
for s in string:
    print (s)

a="apple"
print(a[-3:-6:-1])

 #如果字符串以'p'结尾，则打印
list_string = ['apple','banana_p','orange','cherry_p']
for fruit in list_string:
    if fruit[-1] == 'p':
        print(fruit)

for fruit in list_string:
    print(fruit.count('a'))

print("shasha".find("a"))

print("shasha".index("a"))

print("and" in "andandand")

for fruit in list_string:
    print(fruit.split("_"))

my_string = ' hello world\n'
print(my_string.strip())

rate=23/56
print("rate is %.2f"%rate)

name = 'Molly'
hight = 170.4
score_math = 95
score_english = 89
print(f"大家好！我叫{name}，我的身高是{hight:.3f} cm, 数学成绩{score_math}分,英语成绩{score_english}分")

for a in list_string:
    print('a'in a)

list1 = ['a','b','a','d','a','f']
print(list1.count('a')) 
print(list1.index('a')) 


list1 = ['a','b','a','d','a','f']
print(['app_%s'%n for n in list1 ])


list1 = ['a','b','a','d','a','f']
[f'app_{n}' for n in list1 ]
print(list1)

print([n for n in range(30) if n%2==0])