import random
import collections
import pickle
import heap
import networkx as nx
import matplotlib.pyplot as plt
import MBP

for __counter__ in range(5):            
    a = MBP.MBP()
    G1 = nx.Graph()
    for e in a.g:
        G1.add_edge(e[0],e[1],weight=a.weight[tuple(e)])
    edges = G1.edges()
    pos = nx.spring_layout(G1)
    weights = [G1[u][v]['weight']/1.5 for u,v in edges]
    with open('pos.pickle', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([edges,pos,weights,G1], f)
    f.close()


    # with open('pos.pickle', 'rb') as f:  # Python 3: open(..., 'wb')
    #     edges,pos,weights,G1 = pickle.load(f)
    # f.close()
    # mbp,v = a.mbp_heap(min(a.graph.keys()),max(a.graph.keys()))
    # for __pair__ in range(5):
    start,end = random.sample(a.graph.keys(),2)
    # paths = a.mbp_heap(5)
    # print(mbp,v)
    # for r in range(len(paths)):
    mbp,v = a.mbp_heap(start,end)
    mbp_edges = []
    for i in range(len(mbp)-1):
        mbp_edges.append([mbp[i],mbp[i+1]])
    G2 = nx.Graph()
    for e in mbp_edges:
        G2.add_edge(e[0],e[1],weight=a.weight[tuple(e)])
    edges2 = G2.edges()
    G3 = nx.Graph()
    G3.add_node(start)
    G3.add_node(end)
    # pos2 = nx.spring_layout(G2)
     # edge_color=weights,
    nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color='blue', width=weights,edge_cmap=plt.cm.Blues)
    nx.draw(G3,pos, node_color = 'r',node_size = 10)
    plt.savefig('mbp_total' + str(__counter__) + '.png')
    # plt.show()
    # plt.close()
    # nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color=weights, width=weights,edge_cmap=plt.cm.Blues)
    nx.draw(G2,pos, node_color = 'r',node_size = 5,edges=edges2, edge_color='r', width=3.0)
    # nx.draw(G3,pos, node_color = 'r',node_size = 10)
    plt.savefig('mbp_path' + str(__counter__) + '.png')
    # plt.show()
    plt.clf()
    a = []
        # plt.show()
        # plt.close()