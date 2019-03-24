    def mbp_heap(self,times):
        self.sall,self.tall,res = [],[],[]
        for i in range(times):
            tmps,tmpt = random.sample(self.graph.keys(),2)
            self.sall.append(tmps)
            self.tall.append(tmpt)
        def track_back(t):
            path = [t]
            mbpv = bw[t]
            while t!= parent[t]:
                path.append(parent[t])
                t = parent[t]
            return path,mbpv
        for s,t in list(zip(self.sall,self.tall)):
            dill.load_session('15000.pkl')
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
            path,v = track_back(t)
            res.append([path,v])
        return res
    def cruscal(self,s,t):
        parent = [i for i in self.graph]
        def root(v):
            while v!=parent[v]:
                v = parent[v]
            return v
        sorted_edges = sorted(self.weight,key=lambda x:self.weight[x])