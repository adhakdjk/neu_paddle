import numpy as np
#数据导入
def load_data():
    datafile=' '
    data=np.fromfile(datafile,sep=' ')#这里的sep代表着分割，例如I like you，会根据空格进行分割，把他们分成I,like,you
    feature_name=['CRIN','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
    feature_num=len(feature_name)

#数据分类
    data=data.reshape([data[0]//feature_num,feature_num])
    ratio=0.8
    offset=int(data.shape[0]*ratio)
    training_data=data[:offset]
    test_date=data[offset:]
    #得出每一个样本数据的最大值和最小值，最后是一个列表形式
    maximums,minimums,avgs=training_data.max(axis=0),training_data.min(axis=0),training_data.sum(axis=0)/training_data.shape[0]#这里的axis=0指的是纵向方向

#数据归一化处理
    for i in range(feature_num):
        data[:,i]=(data[:,i]-minimums[i])/(maximums[i]-minimums[i])

    training_data=data[:offset]
    test_data=data[offset:]
    return training_data, test_data

#获取数据
training_data,test_data=load_data()
x=training_data[:,:-1]
y=training_data[:,-1:]

#模型设计
import random
class Network(object):
    #生成w和b
    def __init__(self,num_of_weights):
        np.random.seed(0)
        self.w=np.random.randn(num_of_weights,1)
        self.b=0

    def forward(self,x):
        z=np.dot(x,self.w)+self.b
        return z
    #损失函数模型：    
    def loss(self,z,y):
        error=z-y
        num_samples=error.shape[0]
        cost=error*error
        cost=np.sum(cost)/num_samples
        #cost=np.mean(cost)
        return cost
    
    #阶梯下降
    def gradient(self,x,y):
        z=self.forward(x)
        gradient_w=(z-y)*x
        gradient_w=np.mean(gradient_w,axis=0)
        gradient_w=gradient_w[:,newaxis]
        #gradient_w=gradient.reshape(13,1)
        gradient_b=(z-y)
        gradient_b=np.mean(gradient_b)
        return gradient_w,gradient_b
    
    #更新梯度
    def update(self,gradient_w,gradient_b,eta=0.01):
        self.w=self.w-eta*gradient_w
        self.b=self.b-eta*gradient_b

    def train(self,x,y,iterations,eta=0.01):
        losses=[]
        for i in range(iterations):
            z=self.forward(x)
            L=self.loss(z,y)
            gradient_w,gradient_b=self.gradient(x,y)
            self.update(gradient_w,gradient_b,eta)
            losses.append(L)
            if(i+50)%10==0:
                print(f'inter{i},loss{L}')
            return losses

#创建网络
net=Network(13)
num_iterations=1000
#开始训练
losses=net.train(x,y,iterations=num_iterations,eta=0.01)

#画出损失函数的变化趋势
plot_x=np.arange(num_iterations)
plot_y=np.array(losses)
plt.plot(plot_x,plot_y)
plt.show()

