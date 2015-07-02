#author:wen
#date:2014-3-31
#description:Create the cooperation map between authors.
#------------------------------------------------------------------------#

import cPickle as pickle
import re

link=pickle.load(file('link.pkl','rb'))
dic=pickle.load(file('dic.pkl','rb'))

authors=[]
for i in dic:
    for j in i['AF']:
        authors.append(j)
authors=list(set(authors))


auid={}
aid=1
for i in authors:
    auid[i]=aid
    aid+=1

def cn2(i):
    """generate the combination of a list elements"""
    comb=[]
    k=0
    for m in i[:-1]:
        for j in i[k+1:]:
            comb.append([auid[i[k]],auid[j]])
            k+=1
    return comb

	
def authorx(i):
    """information of a certain author i ,return a list in the order of \
	his paper records, the number of paper count, the year when he step in,\
	the year when he quit, and impactor of his papers"""
    isp=[]
    for p in dic:
        if i in p['AF']:
            isp.append(p)
    amount=len(isp)
    yearange=[i['PY'] for i in isp]
    yearange.sort()
    inyear=yearange[0]
    outyear=yearange[-1]
    ifactor=0
    for p in isp:
        ifactor+=p['CI']
    return [isp,amount,inyear,outyear,ifactor]


def co_au_map(node,edge,nodefile,edgefile):
    """create the cooperation map till now"""
    fnode=open(nodefile+'.csv','w')
    fnode.write('Id;Label\n')
    for i in node:
        fnode.write(str(i[0])+';'+i[1]+'\n')
    fnode.close()
    fedge=open(edgefile+'.csv','w')
    fedge.write('Source;Target;Type\n')
    for i in edge:
        fedge.write(str(i[0])+';'+str(i[1])+';'+'Undirected\n')
    fedge.close()


def evo_au_map(year):
    """create the cooperation map till certain year"""
    papers=[]
    node=[]
    edge=[]
    for i in dic:
        if int(i['PY'])<=year:
            papers.append(i)
    for i in papers:
        for j in i['AF']:
            if (auid[j],j) not in node:
                node.append((auid[j],j))
        edge.extend(cn2(i['AF']))
    co_au_map(node,edge,str(year)+' aunode',str(year)+' auedge')

