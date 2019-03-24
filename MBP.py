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
    def kruscal(self,s,t):
        print(s,t)
        # initialize the parent of each point
        parent = [i for i in range(self.size)]
        dad = [i for i in range(self.size)]
        count = [1 for i in range(self.size)]
        bw = [float('inf') for i in range(self.size)]
        def root(v):
            while v!=parent[v]:
                v = parent[v]
            return v
        def track(v):
            path = [v]
            while dad[v]!=v:
                path.append(dad[v])
                v = dad[v] 
            path.append(s)
            print(path)
            return path
        self.g = sorted(list(self.g),key = lambda x:self.weight[x],reverse=True)
        for e in self.g:
            r0,r1 = root(e[0]),root(e[1])
            if r0!=r1:
                if count[e[0]]>count[e[1]]:
                    parent[r1] = r0
                    dad[e[1]] = e[0]
                    count[e[0]] += count[e[1]]
                    bw[r0] = min(bw[r0],self.weight[e])
                else:
                    parent[r0] = r1
                    dad[e[0]] = e[1]
                    count[e[1]] += count[e[0]]
                    bw[r1] = min(bw[r1],self.weight[e])
            # if e[0]==t or e[1]==t:
            #     break

        return track(t),bw[root(t)]
    def Mid(self,nums,target):
        # def partition_median(nums):
        p = random.sample(list(range(len(nums))),1)[0]
        val = nums[p]
        nums[p],nums[-1]=nums[-1],nums[p]
        i = -1
        ct = 0
        for j in range(len(nums)-1):
            if nums[j]<val:
                ct += 1
                i += 1
                nums[j],nums[i] = nums[i],nums[j]
        i += 1
        nums[-1],nums[i] = nums[i],nums[-1]
        if ct == target:
            return nums
        elif ct>target:
            return self.Mid(nums[:ct],target) + nums[ct:]
        else:
            return nums[:ct] + self.Mid(nums[ct:],target-ct)

        # return ct,nums

        # sorted_edges = sorted(self.weight,key=lambda x:self.weight[x])
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




    # # test Kruscal

    # a = MBP()
    # print(a.g)
    # G1 = nx.Graph()
    # for e in a.g:
    #     G1.add_edge(e[0],e[1],weight=a.weight[tuple(e)])
    # edges = G1.edges()
    # pos = nx.spring_layout(G1)
    # weights = [G1[u][v]['weight']/8 for u,v in edges]
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
    
    # mbp,v = a.kruscal(start,end)
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
    # nx.draw(G1,pos, node_color = 'g',node_size = 5,edges=edges, edge_color='black', width=weights,edge_cmap=plt.cm.Blues)
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



    # test linear algorithm to find medians
    a = MBP()
    res = []
    for i in range(1000):
        l = random.sample(list(range(150)),int(149*random.random())+1)
        # print(l)
        mid = sorted(l)[len(l)//2]
        b = a.Mid(l,len(l)//2)
        # c = dir(b)
        res.append(b[len(l)//2]!=mid)
    print(any(res))