#author:wen
#date:2014-3-13
#description:Extract the authors, publish year, publication source 
#            and its reference papers from the endnote file.
#------------------------------------------------------------------------#

import re

n=2468

#正则匹配式
pattern_au=r'AU\s{1}(.*)'
pattern_py=r'PY\s{1}(\d+)'
pattern_j9=r'J9\s{1}(.*)'
pattern_cr = r'([\w\s\-\.]+),\s(\d{4}),\s([0-9a-zA-Z\s\-\(\)\*]+)(,|$)'

#打开边文件，记录文献引用关系
edgefile=open('edgefile.txt','w')
edgefile.write('Sourse;Target\n')

#对每一行进行匹配，保存成{AU,PY,J9}字典的形式，并在edgefile中记录引用关系
for i in range(1,n):
    fs=open('ER'+str(i)+'.txt','r')
    fr=open('recdirfile.txt','a')
    selfdir={}
    crlist=[]
    for line in fs.readlines():
        if line.startswith('CR '):
            line = line[3:]
        match_au = re.match(pattern_au,line)
        match_py = re.match(pattern_py,line)
        match_j9 = re.match(pattern_j9,line)
        match_cr = re.match(pattern_cr,line.strip())
        if match_cr:
            crlist.append({'AU':match_cr.group(1),'PY':match_cr.group(2),\
                           'J9':match_cr.group(3)})
        if match_au:
            selfdir['AU']=match_au.group(1)
        if match_py:
            selfdir['PY']=match_py.group(1)
        if match_j9:
            selfdir['J9']=match_j9.group(1)
    recdir={'SELF':selfdir,'CR':crlist}
    for ele in recdir['CR']:
        edgefile.write(str(recdir['SELF'])+';'+str(ele)+'\n')
    fr.write(str(recdir)+'\n')
    fs.close()
    fr.close()
    
edgefile.close()
print('抽取结束!')
