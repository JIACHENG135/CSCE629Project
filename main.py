import networkx as nx
import matplotlib.pyplot as plt
import random
import collections
import dill

class Solution(object):
    def __init__(self):
        self.counter = collections.defaultdict(int)
        self.g = set()
        self.weight = collections.defaultdict(int)
        for i in range(4999):
            self.g.add(tuple([i,i+1]))
            self.weight[tuple([i,i+1])] = random.uniform(1,10)
            self.counter[i] += 1
            self.counter[i+1] += 1
    def gene_graph_sparse(self):
        while len(self.g)<15000:
            a = int(5000*random.random())
            b = int(5000*random.random())
            c = random.uniform(1,10)
            if a!=b and (a,b) not in self.g and (b,a) not in self.g:
                self.g.add(tuple([a,b]))
                self.counter[a] += 1
                self.counter[b] += 1
                self.weight[tuple([a,b])] = c
        return self.g
    def gene_graph_dense(self):
        for a in range(5000):
            wait = list(range(a)) + list(range(a+1,5000))
            picked = random.sample(wait,  int(0.2*5000))
            for b in picked:
                print(a==b)

                self.g.add(tuple([a,b]))
                self.counter[a] += 1
                self.counter[b] += 1
                self.weight[tuple([a,b])] = random.uniform(1,10)
        return self.g
    def save(self):
        dill.dump_session('15000.pkl')
if __name__ == '__main__':
    a = Solution()
    # dill.load_session('15000.pkl')
    # b = a.gene_graph_sparse()
    b = a.gene_graph_dense()
    G = nx.Graph()

    # for e in b:
    #     G.add_weighted_edges_from([(e[0],e[1],a.weight[e])])
    

    # plt.plot(a.counter.keys(), a.counter.values())
    # plt.show()
    
    edge_counter = [0 for i in range(max(a.counter.values())+1)]
    for v in a.counter.values():
        edge_counter[v] += 1

    plt.plot(list(range(max(a.counter.values())+1)), edge_counter,'ro')
    plt.show()

