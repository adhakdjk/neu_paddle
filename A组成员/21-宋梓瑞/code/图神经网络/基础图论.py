import numpy as np
import pandas as pd
import networkx as nx

edges=pd.DataFrame()
edges['source']=[1,1,1,2,2,3,3,4,4,5,5,5]
edges['target']=[2,4,5,3,1,2,5,1,5,1,3,4]
edges['weights']=[1,1,1,1,1,1,11,1,1,1,1]

G=nx.from_pandas_edgelist(edges,source='sources',target='target',edge_attr='weigthts')
#degree

print(nx.degree(G))


#连通分量
#连通分量∶无向图G的一个极大连通子图称为G的一个连通分量（或连通分支)。连通图只有一个连通分量，即其自身;非连通的无向图有多个连通分量。

print(nx.connected_components(G))




#图直径
print(nx.diameter(G))

#度中心性
##
# 设想一下，你在微信上有个账号，那么是不是意味着微信好友数量越多，那么你的社交圈子越广？（假设都是真实好友，不考虑微商神马的奇葩情况）比如我有20个好友，
# 那么意味着20个结点与我相连。如果你有50个好友
# 那么意味着你的点度中心度比我高，社交圈子比我广。这个就是点度中心性的概念。
# 当然，刚才这个情况是无向图的情形，如果是有向图，需要考虑的出度和入度的问题。
print(nx.degree_centrality(G))

#特征向量中心性
#特征向量中心性的基本思想是，一个节点的中心性是相邻节点中心性的函数
print(nx.eigenvector_centrality(G))




#betweenness
#中介中心性指的是一个结点担任其它两个结点之间最短路的桥梁的次数。一个结点充当“中介”的次数越高，它的中介中心度就越大。
# 如果要考虑标准化的问题，可以用一个结点承担最短路桥梁的次数除以所有的路径数量。
print(nx.betweenness_centrality(G))



#closeness
#接近中心性需要考量每个结点到其它结点的最短路的平均长度。也就是说，对于一个结点而言，它距离其它结点越近，那么它的中心度越高。
# 一般来说，那种需要让尽可能多的人使用的设施，它的接近中心度一般是比较高的
print(nx.closeness_centrality(G))



#pagerank
#假设一个由只有4个页面组成的集合：A，B，C和D。如果所有页面都链向A，那么A的PR（PageRank）值将是B，C及D的和。
print(nx.pagerank(G))

#HITS
#HITS算法的全称是Hyperlink-Induced Topic Search。在HITS算法中，每个页面被赋予两个属性：hub属性和authority属性。同时，网页被分为两种：hub页面和authority页面。
#hub，中心的意思，所以hub页面指那些包含了很多指向authority页面的链接的网页，比如国内的一些门户网站；authority页面则指那些包含有实质性内容的网页


#        页面hub值等于所有它指向的页面的authority值之和。
#        页面authority值等于所有指向它的页面的hub值之和。



print(nx.hits(G))
