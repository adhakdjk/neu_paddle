# python 中的items()

>以列表返回可遍历的(key,values)元组。  


  
``` python 
favorite_places = {'XiaoMing': 'TJL','XiaoQiang':'Amercia','Dongsheng':'Japan'}
print("数值:%s" % favorite_places.items())
for key,value in favorite_places.items():
    print(key,value)
```


>数值:dict_items([('XiaoQiang', 'Amercia'), ('Dongsheng', 'Japan'), ('XiaoMing', 'TJL')])  
XiaoQiang Amercia   
Dongsheng Japan  
XiaoMing TJL  


# torch.optim.lr_scheduler

>torch.optim.lr_scheduler模块提供了一些根据epoch训练次数来调整学习率（learning rate）的方法。一般情况下我们会设置随着epoch的增大而逐渐减小学习率从而达到更好的训练效果。
而torch.optim.lr_scheduler.ReduceLROnPlateau则提供了基于训练中某些测量值使学习率动态下降的方法。


``` python
    torch.optim.lr_scheduler: #根据学习率更新次数调整学习率
    torch.optim.lr_scheduler.ReduceLROnPlateau：#根据验证集的评价指标调整学习率
```
# ipynb 快捷键
Enter : 转入编辑模式
Shift-Enter : 运行本单元，选中下个单元
Ctrl-Enter : 运行本单元
Alt-Enter : 运行本单元，在其下插入新单元
Y : 单元转入代码状态
M :单元转入markdown状态
R : 单元转入raw状态
1 : 设定 1 级标题
2 : 设定 2 级标题
3 : 设定 3 级标题
4 : 设定 4 级标题
5 : 设定 5 级标题
6 : 设定 6 级标题
Up : 选中上方单元
K : 选中上方单元
Down : 选中下方单元
J : 选中下方单元
Shift-K : 扩大选中上方单元
Shift-J : 扩大选中下方单元
A : 在上方插入新单元
B : 在下方插入新单元
X : 剪切选中的单元
C : 复制选中的单元
Shift-V : 粘贴到上方单元
V : 粘贴到下方单元
Z : 恢复删除的最后一个单元
D,D : 删除选中的单元
Shift-M : 合并选中的单元
Ctrl-S : 文件存盘
S : 文件存盘
L : 转换行号
O : 转换输出
Shift-O : 转换输出滚动
Esc : 关闭页面
Q : 关闭页面
H : 显示快捷键帮助
I,I : 中断Notebook内核
0,0 : 重启Notebook内核
Shift : 忽略
Shift-Space : 向上滚动
Space : 向下滚动
回到顶部
二、编辑模式 ( Enter 键启动)

Tab : 代码补全或缩进
Shift-Tab : 提示
Ctrl-] : 缩进
Ctrl-[ : 解除缩进
Ctrl-A : 全选
Ctrl-Z : 复原
Ctrl-Shift-Z : 再做
Ctrl-Y : 再做
Ctrl-Home : 跳到单元开头
Ctrl-Up : 跳到单元开头
Ctrl-End : 跳到单元末尾
Ctrl-Down : 跳到单元末尾
Ctrl-Left : 跳到左边一个字首
Ctrl-Right : 跳到右边一个字首
Ctrl-Backspace : 删除前面一个字
Ctrl-Delete : 删除后面一个字
Esc : 进入命令模式
Ctrl-M : 进入命令模式
Shift-Enter : 运行本单元，选中下一单元
Ctrl-Enter : 运行本单元
Alt-Enter : 运行本单元，在下面插入一单元
Ctrl-Shift-- : 分割单元
Ctrl-Shift-Subtract : 分割单元
Ctrl-S : 文件存盘
Shift : 忽略
Up : 光标上移或转入上一单元
Down :光标下移或转入下一单元
————————————————
版权声明：本文为CSDN博主「wblylh」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wblylh/article/details/116455240


# GPUtil是一个Python模块，使用nvidia-smi从NVIDA GPU获取GPU状态


# torch.mutilprocessing
[https://cloud.tencent.com/developer/article/1994697](https://cloud.tencent.com/developer/article/1994697)
> 用来多进程处理的

# numpy.flatten()
>a.flatten()：a是个数组，a.flatten()就是把a降到一维，默认是按行的方向降 。
a.flatten().A：a是个矩阵，降维后还是个矩阵，矩阵.A（等效于矩阵.getA()）变成了数组。
``` python
a = [[1,3],[2,4],[3,5]]
a = array(a)
a.flatten()
array([1, 3, 2, 4, 3, 5])


```

# torch.triu
[triu用法及代码实例](https://vimsky.com/examples/usage/python-torch.triu-pt.html)

# squeeze( ) 和unsqueeze( )函数功能和使用


# zip()
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。(注：在python3中返回的是zip对象)
``` python
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
print([i for i in zip(list1, list2)])
"""
result:
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 0)]
"""
```








