#author:wen
#date:2014-4-23
#description:在进行姓名消歧的过程中，首先生成一个文件包含了初始的所有姓名，
#            处理过程中，我们会不断发现多个姓名实际上指代同一个作者的情况，
             可以将这些姓名写在一个临时的姓名替换文件中，并且将初始文件相
             应的姓名替换成统一形式，最后对所有的文件版本进行处理，即可得
             到一个姓名词典，用于名字统一。
#------------------------------------------------------------------------#

def rep_word(word,word_dict):
    buff=[]
    for item in word_dict:
        if word in item:
            buff.append( item[0])
    if buff ==[]:
        return word
    else:
        return buff[0]
    
def rep_names(old_version_file,new_version_file,rep_dic_file):
    f_old=open(old_version_file,'r')
    old_list=[i[:-1] for i in f_old.readlines()]
    f_old.close()
    f_rep=open(rep_dic_file,'r')
    word_dict=[i[:-1].split(';') for i in f_rep.readlines()]
    f_rep.close()
    new_list=[]
    for i in old_list:
        new_list.append(rep_word(i,word_dict))
    f_new=open(new_version_file,'w')
    for i in new_list:
        f_new.write(i+'\n')
    f_new.close()
