#author:wen
#date:2014-3-31
#description:Create the citation relationship map between certain authors 
#            along the year.
#------------------------------------------------------------------------#

import cPickle as pickle

# 载入文献引用关系和文献信息
link=pickle.load(file('link.pkl','rb'))
dic=pickle.load(file('dic.pkl','rb'))

# authors为作者名并去重
authors=[]
for i in dic:
    for j in i['AF']:
        authors.append(j)
authors=list(set(authors))

# 为作者编号
auid={}
aid=1
for i in authors:
    auid[i]=aid
    aid+=1

def edge_weight(edge):
  """compute the weight of all edges"""
  newedgedir={}
  for i in edge:
    if i not in newedgedir:
    	newedgedir[i]=1
    else:
        newedgedir[i]+=1
  newedge=[(i[0],i[1],newedgedir[i]) for i in newedgedir.keys()]
  return newedge


def a2b(lin):
    """each link have two papers, the source and the target, and each paper
       is coauthored by more than one scientists, this function is used to
       generated all the edges from the source-authors to the target-authors"""
    for i in dic:
        if i['ID']==int(lin[0]):
            au1=i['AF']
    for i in dic:
        if i['ID']==int(lin[1]):
            au2=i['AF']
    a2bedge=[]
    for i in au1:
        for j in au2:
            a2bedge.append((auid[i],auid[j]))
    return a2bedge
	
def au_cit_map(node,edge,nodefile,edgefile):
    """get the csv format file of nodes and edges"""
    fnode=open(nodefile+'.csv','w')
    fnode.write('Id;Label\n')
    for i in node:
        fnode.write(str(i[0])+';'+i[1]+'\n')
    fnode.close()
    fedge=open(edgefile+'.csv','w')
    fedge.write('Source;Target;Type;Weight\n')
    for i in edge:
        fedge.write(str(i[0])+';'+str(i[1])+';'+'Directed'+';'+str(i[2])+'\n')
    fedge.close()

def evo_au_citmap(year):
    """get the author citation map file until certain year"""
    papers=[]
    lnode=[]
    ledge=[]
    edge=[]
    for i in link:
        for j in dic:
            if str(j['ID'])==i[0] and int(j['PY'])<=year:
                ledge.append(i)		
    for i in ledge:
        edge.extend(a2b(i))
    edge=edge_weight(edge)
    for i in ledge:
        papers.extend(i)
    papers=list(set(papers))
    for i in papers:
        for j in dic:
            if j['ID']==int(i):
                lnode.extend(j['AF'])
    lnode=list(set(lnode))
    node=[(auid[i],i) for i in lnode]				
    au_cit_map(node,edge,str(year)+' cunode',str(year)+' cuedge')
