import networkx as nx
import matplotlib.pyplot as plt
import random
import collections
import dill
import heap
__counter__ = 1
__pair__ = 1
class Solution(object):
    def __init__(self,x):
        self.counter = collections.defaultdict(int)
        self.g = set()
        self.weight = collections.defaultdict(int)
        self.graph = collections.defaultdict(set)
        self.size = x
        for i in range(x-1):
            self.g.add(tuple([i,i+1]))
            self.graph[i].add(i+1)
            self.graph[i+1].add(i)
            self.weight[tuple([i,i+1])] = random.uniform(1,10)
            self.counter[i] += 1
            self.counter[i+1] += 1
    def gene_graph_sparse(self):
        while len(self.g)<3*self.size:
            a = int(self.size*random.random())
            b = int(self.size*random.random())
            c = random.uniform(1,10)
            if a!=b and (a,b) not in self.g and (b,a) not in self.g:
                self.graph[a].add(b)
                self.graph[b].add(a)
                self.g.add(tuple([a,b]))
                self.counter[a] += 1
                self.counter[b] += 1
                self.weight[tuple([a,b])] = c
        return self.g
    def gene_graph_dense(self):
        for a in range(self.size-1):
            wait = list(range(a)) + list(range(a+1,self.size))
            picked = random.sample(wait,  int(0.2*self.size))
            for b in picked:
                self.graph[a].add(b)
                self.graph[b].add(a)
                self.g.add(tuple([a,b]))
                self.counter[a] += 1
                self.counter[b] += 1
                self.weight[tuple([a,b])] = random.uniform(1,10)
        return self.g
    def save(self):
        dill.dump_session('15000.pkl')
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
                    fringe.add(nei)
        return track_back(t)
    def cruscal(self,s,t):
        parent = [i for i in self.graph]
        def root(v):
            while v!=parent[v]:
                v = parent[v]
            return v
        sorted_edges = sorted(self.weight,key=lambda x:self.weight[x])
if __name__ == '__main__':


    # gene picture for heap_mbp

    # for __counter__ in range(3):
    a = Solution(30)
    b = a.gene_graph_dense()
    G1 = nx.Graph()
    for e in a.g:
        G1.add_edge(e[0],e[1],weight=a.weight[tuple(e)])
    edges = G1.edges()
    pos = nx.spring_layout(G1)
    weights = [G1[u][v]['weight']/5 for u,v in edges]

    # mbp,v = a.mbp_heap(min(a.graph.keys()),max(a.graph.keys()))
    # for __pair__ in range(5):
    start,end = random.sample(a.graph.keys(),2)
    mbp,v = a.mbp_heap(start,end)
    print(mbp,v)
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
    nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color=weights, width=weights,edge_cmap=plt.cm.Blues)
    nx.draw(G3,pos, node_color = 'r',node_size = 10)
    plt.savefig('mbp_total' + str(__counter__) +'#' + str(__pair__) + '.png')
    # plt.show()
    # plt.close()
    # nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color=weights, width=weights,edge_cmap=plt.cm.Blues)
    nx.draw(G2,pos, node_color = 'r',node_size = 5,edges=edges2, edge_color='r', width=3.0)
    # nx.draw(G3,pos, node_color = 'r',node_size = 10)
    plt.savefig('mbp_path' + str(__counter__) +'#' + str(__pair__) + '.png')
    plt.clf()
    # plt.show()
    # plt.close()



    # generate plot for points counter sparse
    # a = Solution(5000)
    # b = a.gene_graph_sparse()
    # for e in b:
    #     G.add_weighted_edges_from([(e[0],e[1],a.weight[e])])
    

    # plt.plot(a.counter.keys(), a.counter.values())
    # plt.show()



    # generate plot for points counter dense
    # a = Solution(5000)
    # edge_counter = [0 for i in range(max(a.counter.values())+1)]
    # for v in a.counter.values():
    #     edge_counter[v] += 1

    # plt.plot(list(range(max(a.counter.values())+1)), edge_counter,'ro')
    # plt.show()




