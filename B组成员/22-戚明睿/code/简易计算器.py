from base64 import b16decode, b16encode
from pickle import NONE
from types import NoneType

calaulator =(0,1,2,3,4,5,6,7,8,9，"+","-","*","/") 
#这里报错了不知道怎么回事
while true
    c_str=""
    a=NONE
    a_string=""
    arithmetic=0
    b=none
    b_string=""
    result=0
    # 初始化
    while true
    t_a=input("请选择键位0-9，或者输入四则运算符")
    if t_a=="="
        arithmetic=-1
        if a_string:
            a=int(a_string)
        else:
            a_string='0'
            a=0
        c_str=a_string+'='
        break
    if t_a=='+':
        c_str=a_string+'+'
        a=int(a_string)
        arithmetic=11
        break
    elif t_a=='-':
        c_str=a_string+'-'
        a=int(a_string)
        arithmetic=12
        break
    elif t_a=='*':
        c_str=a_string+'*'
        a=int(a_string)
        arithmetic=13
        break
    elif t_a=='/':
        c_str=a_string+'/'
        a=int(a_string)
        arithmetic=14
        break
    elif int(t_a) in range(0,10)
    a_string=a_string+str(calculator[int(t_a)])
    else:
        print("输入错误")
        continue
    print("算式为："，c_str)
    if arithmetic==-1:
        print(c_str,a)
        continue
    while True:
        t_b=input("请输入数据或者=")
        if t_b=='=':
            c_str=c_str+b_string
            if b_string:
                b=int(b_string)
            else:
                b=0
                c_str=c_str+'0'
            c_str=c_str+'='
            if arithmetic==11:
                result=a+b
                print(c_str,result)
            elif arithmetic==12:
                result=a-b
                print(c_str,result)
            elif arithmetic==13:
                result=a*b
                print(c_str,result)
            elif arithmetic==14:
                result=a/b
                print(c_str,result)
            else:
                print("报错了")
            break
        if int(t_b) in range(0,10)
            b_string=b_string+str(calculator[int(t_b)])
        else:
            print("输入错误")
            comtinue
