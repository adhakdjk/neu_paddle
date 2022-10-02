import paddle.fluid as fluid
class SentimentClassifier(fluid.Layer):
    def __init__(self,hidden_size,vocab_size,class_num=2,num_layers=1,num_steps=128,init_scale=0.1,dropout=None):
        super(SentimentClassifier,self).__init__()
        self.hidden_size=hidden_size
        self.vocab_size=vocab_size
        self.class_num=class_num
        self.init_scale=init_scale
        self.num_layers=num_layers
        self.num_steps=num.num_steps
        self.dropout=dropout


        self.simple_lstm_rnn=SimpleLSTMRNN(
            hidden_size,num_steps,num_layers=num_layers,init_scale=init_scale,dropout
        )
        self.Embedding=Embedding(size=[vocab_size,hidden_size],dtype='float32',is_sparse=False,param_attr==fluid.ParamAttr(name='embedding_para',initializer=fluid.initializer.UniformInitializer(low=-init_scale,high=init_scale))
        self.softmax_weight=self.create_parameter(attr=fluid.ParamAttr(),shape=[self.hidden_size,self.class_num],dtype="float32",default_initializer=fluid.initializer.UniformInitializer(low=-self.init_scale,high=self.init_scale
            ))
        
        
        )



        self.softmax_bias=self.create_parameter(attr=fluid.ParamAttr(),shape=[self.class_num],dtype='float32',default_initializer=fluid.initializer.UniformInitializer(
            low=-self.init_scale,high=self.init_scale 
    ))