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