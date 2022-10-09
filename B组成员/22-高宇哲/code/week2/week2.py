
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