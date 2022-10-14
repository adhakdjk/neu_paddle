import numpy as np
import random
def load_data():
    file=' '
    data=np.fromfile(file,sep=' ')
    feature_name=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    feature_num=len(feature_name)
    data=data.reshape(data.shape[0]//feature_num,feature_num)

    max=training_data.max(axis=0)
    min=training_data.min(axis=0)
    avg=training_data.mean(axis=0)
    for i in range(feature_name):
        data[:,i]=(data[:,i]-min[i])/(max[i]-min[i])
    
    radio=0.8
    apart=radio*data.shape[0]
    training_data=data[:apart,:]
    test_data=data[apart:,:]
    return training_data,test_data

training_data,test_data=load_data()
x=training_data[:,:-1]
y=training_data[:,-1:]

class Network:
    def __init__(self,num_of_weight):
        np.random.seed(0)
        self.w=np.random.randn(num_of_weight,1)
        self.b=0

    def forward(x):
        z=np.dot(x,self.w)+self.b
        return z

    def Loss():
        error=z-y
        loss=error*error
        loss=loss.mean(axis=0)

    def gradient():
        


        