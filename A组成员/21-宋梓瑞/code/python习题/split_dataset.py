#!/usr/bin/env python

import argparse
import random
import itertools
from os import listdir
import numpy as np
from PIL import Image

RNG_SEED = 56961

#调节参数控制训练集数据的占比

TRAIN_RATION=0.9

CLASSES=('background','road',)
 

def write_rel_paths(phase,names,out_dir):

    tar_path= osp.join(out_dir, phase+'.txt' )
    with open(tar_path,'w') as f:
        for name in names:
            f.write(
                ' '.join([
                    osp.join(prefix,"input",name),
                    osp.join(prefix,'output',name)
                ])
            )
            f.write("\n")
    return tar_path



def binary_to_pseudocolor(path):
    im=Image.open(path)
    im=np.array(im)
    im.clip(0,1,out=im)
    im=Image.fromarray(im,mode='P')
    im.putpalette([0,0,0,255,255,255])
    im.save(path)

if __name__=='__main__':
    random.seed(RNG_SEED)

    parser=argparse.ArgumentParser()
    parser.add_argument('--data_root',type=str,default="./")
    parser.add_argument('--bin_to_pc',action='store_ture', help="二值图转换为伪彩色图像")
    parser.add_argument('labels',type=str,nargs='+',default=['background','foreground'])
    args=parser.parse_args()

    print("开始划分数据集")
    train_prefix='training'
    test_prefix='testing'
    train_names=listdir(osp.join(args.data_root,train_prefix,'output'))
    train_names=list(filter(lambda n: n.endswith('.png'),train_names))
    test_names=listdir(osp.join(args.data_root,test_prefix,'output'))
    test_names=list(filter(lambda n: n.endswith('.png'),test_names))

    train_names.sort()
    test_names.sort()
    random.shuffle(train_names)
    len_train=int(len(train_names)*TRAIN_RATION)
    train_list_path=write_rel_paths("train",train_names[:len_train],args.data_root,train_prefix)
    val_list_path=write_rel_paths("val",train_names[len_train:],args.data_root,train_prefix)
    test_list_path=write_rel_paths('test',test_names,args.data_root,test_prefix)

    if args.bin_to_pc:
        #转换标签文件
        print("开始转换标签文件")
        with open(train_list_path,'r') as f1, open(val_list_path,'r') as f2,open(test_list_path,'r') as f3:
            for line in itertools.chain(f1,f2,f3):
                p=line.strip().split()[1]
                binary_to_pseudocolor(osp.join(args.data_root,p))
    
    print("开始写入信息/....")
    with open(osp.join(args.data_root,'label_txt'),'w') as f:
        for cls in args.labels:
            f.write(cls+'\n')
    
    print ("数据集划分完成")
