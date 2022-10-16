def factor(max_num):
    # 这是一个函数  用于输出所有小于max_num的质数
    factor_list = []
    n = 2
    while n<max_num:
        find = False
        for f in factor_list:
            if n % f == 0:
                find = True
                break
        if not find:
            factor_list.append(n)
            yield n
        n+=1
g=factor(50)
for i in g:
     print(i)

#print[factor_list]

