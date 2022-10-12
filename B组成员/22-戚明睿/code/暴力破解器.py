import time
pwd =input("输入6位目标字符串")
count=0 #计数器
start="0000000" #初始化
time_start=time.perf_counter()
while True:
    if start==pwd:
        print("一共尝试了%d次"%count)
        print("字符串为：%s"%start)
        break
    else:
        start=int(start)+1
        start=((6-int(len(str(start))))*'0')+str(start)
        count+=1
time_end=time.perf_counter()
print('运行时间：%s 秒'%(time_end-time_start))
#此段代码还是报了错我也不太理解
