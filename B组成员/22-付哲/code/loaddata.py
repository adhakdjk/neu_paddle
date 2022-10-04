import numpy as np
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
    maximums,minimums,avgs=training_data.max(axis=0),training_data.min(axis=0),training_data.sum(axis=0)/training_data.shape[0]#这里的axis=0指的是第一排

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

