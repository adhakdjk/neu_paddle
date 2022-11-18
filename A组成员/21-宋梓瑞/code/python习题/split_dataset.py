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
    train_names=listdir(osp.)