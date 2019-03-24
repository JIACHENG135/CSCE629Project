import random
import collections
import pickle
import heap
import networkx as nx
import matplotlib.pyplot as plt
__counter__ = 4
class MBP(object):
    def __init__(self):
        with open('graph_15000.pickle', 'rb') as f:  # Python 3: open(..., 'wb')
            self.graph,self.weight,self.g,self.size = pickle.load(f)
        f.close()
        # self.size = len(self.g)
    def mbp_heap(self,s,t):
        def track_back(t):
            path = [t]
            mbpv = bw[t]
            while t!= parent[t]:
                path.append(parent[t])
                t = parent[t]
            return path,mbpv
        status = [0 for i in range(self.size)]
        bw = [0 for i in range(self.size)]
        bw[s] = float('inf')
        status[s] = 2
        fringe = set()
        parent = list(range(self.size))
        h = heap.max_heap()
        for j in self.graph[s]:
            fringe.add(j)
            status[j] = 1
            parent[j] = s
            bw[j] = self.weight[(s,j)]     
            h.heappush(tuple([bw[j],j]))
        while fringe:
            maxfringe = h.heappop()[1]
            fringe.remove(maxfringe)
            status[maxfringe] = 2
            for nei in self.graph[maxfringe]:
                if status[nei]==0:
                    print('unseen')
                    bw[nei] = min(bw[maxfringe],self.weight[(maxfringe,nei)])
                    fringe.add(nei)
                    h.heappush(tuple([bw[nei],nei]))
                    status[nei] = 1
                    parent[nei] = maxfringe
                elif status[nei]==1 and bw[nei]<min(bw[maxfringe],self.weight[(maxfringe,nei)]):
                    print('fringe')
                    parent[nei] = maxfringe
                    bw[nei] = min(bw[maxfringe],self.weight[(maxfringe,nei)])
                    h.delete(nei)
                    h.heappush(tuple([bw[nei],nei]))
                    # fringe.add(nei)

        return track_back(t)
    def cruscal(self,s,t):
        parent = [i for i in self.graph]
        def root(v):
            while v!=parent[v]:
                v = parent[v]
            return v
        sorted_edges = sorted(self.weight,key=lambda x:self.weight[x])
if __name__ == '__main__':
    # # Heap Part for Dijkstra
    # a = MBP()
    # G1 = nx.Graph()
    # for e in a.g:
    #     G1.add_edge(e[0],e[1],weight=a.weight[tuple(e)])
    # edges = G1.edges()
    # pos = nx.spring_layout(G1)
    # weights = [G1[u][v]['weight']/1.5 for u,v in edges]
    # with open('pos.pickle', 'wb') as f:  # Python 3: open(..., 'wb')
    #     pickle.dump([edges,pos,weights,G1], f)
    # f.close()


    # # This part works fine for Heap MBP Dijkstra


    # # with open('pos.pickle', 'rb') as f:  # Python 3: open(..., 'wb')
    # #     edges,pos,weights,G1 = pickle.load(f)
    # # f.close()
    # # mbp,v = a.mbp_heap(min(a.graph.keys()),max(a.graph.keys()))
    # # for __pair__ in range(5):
    # start,end = random.sample(a.graph.keys(),2)
    # # paths = a.mbp_heap(5)
    # # print(mbp,v)
    # # for r in range(len(paths)):
    # mbp,v = a.mbp_heap(start,end)
    # mbp_edges = []
    # for i in range(len(mbp)-1):
    #     mbp_edges.append([mbp[i],mbp[i+1]])
    # G2 = nx.Graph()
    # for e in mbp_edges:
    #     G2.add_edge(e[0],e[1],weight=a.weight[tuple(e)])
    # edges2 = G2.edges()
    # G3 = nx.Graph()
    # G3.add_node(start)
    # G3.add_node(end)
    # # pos2 = nx.spring_layout(G2)
    #  # edge_color=weights,
    # nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color='blue', width=weights,edge_cmap=plt.cm.Blues)
    # nx.draw(G3,pos, node_color = 'r',node_size = 10)
    # plt.savefig('mbp_total' + str(__counter__) + '.png')
    # # plt.show()
    # # plt.close()
    # # nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color=weights, width=weights,edge_cmap=plt.cm.Blues)
    # nx.draw(G2,pos, node_color = 'r',node_size = 5,edges=edges2, edge_color='r', width=3.0)
    # # nx.draw(G3,pos, node_color = 'r',node_size = 10)
    # plt.savefig('mbp_path' + str(__counter__) + '.png')
    # # plt.show()
    # plt.clf()
    # a = []
    #     # plt.show()
    #     # plt.close()


    