#author:wen
#date:2014-4-12
#description:为了提高研究的准确性，需要进行姓名消歧方面的处理，数据中提供
#            了作者姓名的简写和全写两种形式，但是两种形式下都有一名多写的
#            情况，这里采用简写全写相对照的方法，分别输出简写相同而全写不
#            同和全写相同简写不同（主要）两种情况，对输出结果辅助人工纠查
#            ，提高后期分析的准确程度。
#------------------------------------------------------------------------#

import os
os.chdir('/home/wen/Experiment/sci-e数据处理终极计划/')

import Data_Catcher
names=Data_Catcher.catcher('/home/wen/Experiment/sci-e数据处理终极计划/论文档案/','ER',2047,['AF','AU'])

def list_pair(a,b):
    return [[a[i],b[i]] for i in range(0,len(a))]

af_names=list(set([i for j in names for i in j['AF']]))
au_names=list(set([i for j in names for i in j['AU']]))

#处理得到全写相同而简写不同的情况    
af_same={}
fu_name_pair=[j for i in names for j in list_pair(i['AF'],i['AU'])]
for i in af_names:
    af_same[i]=[]
    for j in fu_name_pair:
        if j[0]==i:
            af_same[i].append(j[1])
    af_same[i]=list(set(af_same[i]))

#处理得到简写相同而全写不同的情况
au_same={}
uf_name_pair=[j for i in names for j in list_pair(i['AU'],i['AF'])]
for i in au_names:
    au_same[i]=[]
    for j in uf_name_pair:
        if j[0]==i:
            au_same[i].append(j[1])
    au_same[i]=list(set(au_same[i]))
