#author:wen
#date:2014-3-31
#description:Use the module networkx to handle the map file and create network
#            graphs.
#------------------------------------------------------------------------#

import sys
import networkx as nx

def swap(i):
    return (i[1],i[0])

def au_edge_weight(edge):
    newedgedir={}
    for i in edge:
        if (i not in newedgedir) and (swap(i) not in newedgedir):
            newedgedir[i]=1
        elif i in newedgedir:
            newedgedir[i]+=1
        elif swap(i) in newedgedir:
            newedgedir[swap(i)]+=1
    newedge=[(i[0],i[1],newedgedir[i]) for i in newedgedir.keys()]
    return newedge

def cit_reader(year):
    """read the csv format files and import the data into networkx to create
       the citation graph"""
    node=[]
    edge=[]
    fnode=open('/media/wen/wen/Data_Resource/Map_Modle/evo-cit-maps/'+\
                str(year)+'map/'+str(year)+' node.csv','r')
    for i in fnode.readlines()[1:]:
        node.append(i[:-1].split(';')[0:2])
    fnode.close()
    fedge=open('/media/wen/wen/Data_Resource/Map_Modle/evo-cit-maps/'+\
                str(year)+'map/'+str(year)+' edge.csv','r')
    for i in fedge.readlines()[1:]:
        edge.append(tuple(i[:-1].split(';')))
    fedge.close()
    G=nx.DiGraph()
    for i in node:
        G.add_node(i[0],label=i[1])
    G.add_edges_from(edge)
    return G

def cau_reader(year):
    """read the csv format files and import the data into networkx to create
       the cooperation graph"""
    node=[]
    edge=[]
    fnode=open('/media/wen/wen/Data_Resource/Map_Modle/evo-au-maps/'+\
                str(year)+'map/'+str(year)+' aunode.csv','r')
    for i in fnode.readlines()[1:]:
        node.append(i[:-1].split(';')[0])
    fnode.close()
    fedge=open('/media/wen/wen/Data_Resource/Map_Modle/evo-au-maps/'+\
                str(year)+'map/'+str(year)+' auedge.csv','r')
    for i in fedge.readlines()[1:]:
        edge.append(tuple(i[:-1].split(';')))
    edge=au_edge_weight(edge)
    G=nx.Graph()
    G.add_nodes_from(node)
    G.add_weighted_edges_from(edge)
    return G
