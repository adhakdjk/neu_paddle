from operator import truediv


g=(x * x for x in range(10))
for n in g:
    print(n)

def rev(a):
    print(a[::-1])
    return 0
b='abcd'
rev(b)

def factor(max):
    list=[]
    n=2
    while n<max:
        find=False
        for i in list:
            if n%i==0:
                find=True
                break
        if not find:
                list.append(n)
                yield n
        n=1+n
g=factor(100)
for m in g:
    print(m)
