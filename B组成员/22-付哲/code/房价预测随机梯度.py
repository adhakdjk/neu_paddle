import json
import numpy as np
import matplotlib.pyplot as plt
#数据导入
def load_data():
    datafile='./work/housing.data'
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

class Network:
    def __init__(self,weight_num):
        np.random.seed(0)
        self.w=np.random.randn(weight_num,1) 
        self.b=0
    def forward(self,x):
        z=np.dot(x,self.w)-self.b
        return z
    def loss(self,y,z):
        error=z-y
        loss=error**2
        loss=np.mean(loss,axis=0)
        return loss
    def gradient(self,y,x):
        z=self.forward(x)
        gradient_w=(z-y)*x
        gradient_w=np.mean(gradient_w,axis=0)
        gradient_w=gradient_w.rashape(13,1)
        gradient_b=z-y
        return gradient_w,gradient_b
    def update(self,gradient_w,gradient_b):   
        eta=0.01
        self.w=self.w-eta*gradient_w
        self.b=self.b-eta*gradient_b

    def train(self,training_data,num_epochs,batch_size=10,eta=0.01):
        n=len(training_data)
        losses=[]
        for epoch_id in range(num_epochs):
            np.random.shuffle(training_data)
            mini_batches=[training_data[k,k+batch_size]for k in range(0,n,batch_size)]
            for iter_id,mini_batch in enumerate(mini_batches):
                x=mini_batch[:,:-1]
                y=mini_batch[:,-1:]
                z=self.forward(x)
                loss=self.loss(y,z)
                gradient_w,gradient_b=self.gradient(y,x)
                self.update(gradient_w,gradient_b)
                losses.append(loss)
            return losses

training_data,test_data=load_data()
net=Network(13)
losses=net.train(training_data,num_epochs=50,batch_size=100,eta=0.1)
plot_x=np.arange(len(losses))
plot_y=np.array(losses)
plt.plot(plot_x,plot_y)
plt.show()






