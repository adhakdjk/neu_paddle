import pandas as pd
import codecs
import os
from PIL import Image
from sklearn.preprocessing import LabelEncoder


all_file_dir = '../work'

train_file = codecs.open(os.path.join(all_file_dir, "train_list.txt"), 'w')
eval_file = codecs.open(os.path.join(all_file_dir, "eval_list.txt"), 'w')

encoder1=LabelEncoder()

housing_cat1=df_train['color']
housing_cat_encoder1=enconder1.fit_transform(housing_cat1)
df_val['color']=pd.DataFrame(housing_cat_encoder1)

housing_cat2=df_train['color']
housing_cat_encoder2=encoder1.fit_transform(housing_cat2)
df_val['color']=pd.DataFrame(housing_cat_encoder2)


train_image_path_list=df_train['id'].values
train_label_list=df_train['color'].values

val_image_path_list=df_val['id'].values
val_label_list=df_val['color'].values

image_path_pre_train='/home/aistudio/data/data147415/vehicle_class/train'
image_path_pre_val='/home/aistudio/data/data147415/vehicle_class/val'

for file,label_id in zip(train_image_path_list,train_label_list):

    try:
        img=Image.open(os.path.join(image_path_pre_train,file))

        train_flie.write("{0}{1}{2}\n".format(file,' ',label_id))

    except Exception as e:
        pass

for file,label_id, in zip(val_image_path_list,val_label_list):

    try:
        img=Image.open(os.path.join(image_path_pre_val,file))

        eval_file.write("{0}{1}{2}\n".format(file,' ',label_id))
    except Exception as e:
        #pass
        print('error')

train_file.close()
eval_file.close()