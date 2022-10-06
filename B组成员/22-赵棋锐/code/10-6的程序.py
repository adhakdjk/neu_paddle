import pandas as pd
import numpy as py
datafile='/home/aistudio/data/titanic.csv'
f=pd.read_csv(datafile)
del f['Name']
del f['Ticket']
del f['Sex']
del f['Cabin']
del f['Embarked']
ceshi_data=f['Age'].dropna()
mean_age=ceshi_data.mean(axis=0)
#print(mean_age)
f['Age']=f['Age'].fillna(mean_age)
f_=py.array(f)
#print(f_)
maxx=f_.max(axis=0)
minn=f_.min(axis=0)
#print(maxx,end=',')
#print(minn,end=',')
avg=f_.mean(axis=0)
for i in range(len(f_[0])):
    f_[:,i]=(f_[:,i]-minn[i])/(maxx[i]-minn[i])
#list
ratio=0.80  #调节测试组数
offset=int(ratio*f.shape[0])
training_data=f_[:offset]
ceshi_data=f_[offset:]
training_data
x=training_data[:,:-1]
y=ceshi_data[:,:-1]
# 设置数学模型
w=[0.1,0.2,0.3,0.4,0.5,0.6]
w=py.array(w).reshape([6,1])
b=-0.2
#print(w)
W=w
class Network(object):
    # 随机化数学模型
    def __init__(self,num_of_weights):
        py.random.seed()
        self.w=py.random.randn(num_of_weights,1)
        print(self.w)
        W=self.w
        self.b=0.
    # 计算函数的预测值
    def forward(self,x):
        z=py.dot(x,self.w)+self.b
        return z
    # 计算函数的损失值
    def loss(self,z,y):
        error=z-y
        cost=error*error
        cost=py.mean(cost)
        return cost,W
        

net=Network(6)
x1=x[0:100]
y1=y[0:100]
z=net.forward(x1)
loss,W=net.loss(z,y1)
print(loss)
print(W)