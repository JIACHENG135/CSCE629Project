import random
class min_heap(object):
    # build min heap
    def __init__(self,nums=[]):
        self.ar = list(range(len(nums)))
        self.D = nums
        self.size = len(nums)
        self.heapfy()
        self.check()
    def heapfy(self):
        for ind in range(self.size):
            if self.D[ind]<self.D[(ind-1)//2]:
                self.switch_up(ind)
    def left(self,ind):
        return 2*(ind+1)-1
    def right(self,ind):
        return 2*(ind+1)
    def switch_down(self,ind):
        l = self.left(ind)
        r = self.right(ind)
        if r<self.size and self.D[r]<self.D[ind]:
            larg = r
        else:
            larg = ind
        if l<self.size and self.D[l]<self.D[larg]:
            larg = l
        if larg!=ind:
            self.ar[ind],self.ar[larg] = self.ar[larg],self.ar[ind]
            self.switch_down(larg)
    def switch_up(self,ind):
        if ind==0:return
        p = int((ind-1)/2)
        if self.D[p]>self.D[ind]:
            self.ar[p],self.ar[ind] = self.ar[ind],self.ar[p]
            self.switch_up(p)
    def delete(self,ind):
        if len(self.ar)==1:
            self.ar.pop()
            return
        # print(self.ar,ind)
        # tmp = self.ar[ind]
        self.ar[ind] = self.ar[self.size-1]
        self.size -= 1
        self.ar.pop()
        if self.D[ind]<self.D[int((ind-1)/2)]:
            self.switch_up(ind)
        else:
            self.switch_down(ind)
    def heappush(self,num):
        self.D.append(num)
        self.ar.append(self.size)
        self.size += 1
        self.switch_up(self.size-1)

    def heappop(self):
        if not self.ar:
            print('pop from an empty heap')
            return
        minv = self.ar[0]
        self.D[0] = self.D[self.size-1]
        self.size -= 1
        self.switch_down(0)
        self.ar.pop()
        self.D.pop()
        return minv
    def check(self,ind):
        if 2*(ind+1)-1<self.size:
            if not self.D[ind]<=self.D[2*(ind+1)-1]:
                print(self.D,self.D[ind],self.D[2*(ind+1)-1])
            self.check(2*(ind+1)-1)
        if 2*(ind+1)<self.size:
            if not self.D[ind]<=self.D[2*(ind+1)]:
                print(self.D[ind],self.D[2*(ind+1)])
            self.check(2*(ind+1))
    

class max_heap(object):
    # build max heap
    def __init__(self,nums=[]):
        self.ar = list(range(len(nums)))
        self.D = nums
        self.size = len(nums)
        self.tracker = {}
        for i in range(self.size):
            self.tracker[self.D[i][1]] = i
        self.heapfy()
        self.check(0)


    def heapfy(self):
        # for ind in range(len(self.ar)-1,-1,-1):
        for ind in range((len(self.ar)-1)//2,-1,-1):
                self.switch_down(ind)
    def left(self,ind):
        return 2*(ind+1)-1
    def right(self,ind):
        return 2*(ind+1)
    def switch_down(self,ind):
        l = self.left(ind)
        r = self.right(ind)
        if l<len(self.ar) and self.D[self.ar[l]]>self.D[self.ar[ind]]:
        # if l<self.size and self.D[self.ar[l]]>self.D[self.ar[ind]]:
            larg = l
        else:
            larg = ind
        if r<len(self.ar) and self.D[self.ar[r]]>self.D[self.ar[larg]]:
            larg = r
        if larg!=ind:
            self.tracker[self.D[self.ar[ind]][1]] = larg
            self.tracker[self.D[self.ar[larg]][1]] = ind
            self.ar[ind],self.ar[larg] = self.ar[larg],self.ar[ind]
            self.switch_down(larg)
    def switch_up(self,ind):
        if ind==0:return
        p = int((ind-1)/2)
        if self.D[self.ar[p]]<self.D[self.ar[ind]]:
            self.tracker[self.D[self.ar[p]][1]] = ind
            self.tracker[self.D[self.ar[ind]][1]] = p
            self.ar[p],self.ar[ind] = self.ar[ind],self.ar[p]
            self.switch_up(p)
    def delete(self,ind):
        if len(self.ar)==1:
            self.ar.pop()
            return
        target = int(ind)
        ind = self.tracker[ind]
        self.tracker[self.D[self.ar[ind]][1]] = len(self.ar)-1
        self.tracker[self.D[self.ar[-1]][1]] = ind
        self.ar[ind] = self.ar[-1]
        self.size -= 1
        if self.D[self.ar[ind]]>self.D[self.ar[int((ind-1)/2)]]:
            self.ar.pop()
            self.switch_up(ind)
        else:
            self.ar.pop()
            self.switch_down(ind)
    def heappush(self,num):
        self.D.append(num)
        self.ar.append(len(self.D)-1)
        self.tracker[self.D[self.ar[-1]][1]] = len(self.ar)-1
        self.switch_up(len(self.ar)-1)
        self.size += 1


    def heappop(self):
        if not self.ar:
            print('pop from an empty heap')
            return              
        minv = self.D[self.ar[0]]
        self.ar[0] = self.ar[-1]
        self.tracker[self.D[self.ar[-1]][1]] = 0
        self.ar.pop()
        self.switch_down(0)
        return minv
    def check(self,ind):
        if 2*(ind+1)-1<len(self.ar):
            if self.D[self.ar[ind]]<self.D[self.ar[2*(ind+1)-1]]:
                print('false',self.D[self.ar[ind]],self.D[self.ar[2*(ind+1)-1]])
            self.check(2*(ind+1)-1)
        if 2*(ind+1)<len(self.ar):
            if self.D[self.ar[ind]]<self.D[self.ar[2*(ind+1)]]:
                print('false',self.D[self.ar[ind]],self.D[self.ar[2*(ind+1)]])
            self.check(2*(ind+1))
    


if __name__ == '__main__':
    # general test for push pop and heapfy

    # test1 = random.sample(list(range(400)),10)
    # test2 = random.sample(list(range(20)),10)
    # test = []
    # pp = max_heap()
    # for i in range(10):
    #     test.append(tuple([test1[i],test2[i]]))
    #     pp.heappush(tuple([test1[i],test2[i]]))
    # lt = list(test)
    # max_h =max_heap(lt)
    # pp.check(0)
    # # print([a.D[i][0] for i in a.ar])
    # poplist2 = []
    # pplist = []
    # while max_h.ar:
    #     poplist2.append(max_h.heappop()[0])
    # while pp.ar:
    #     pplist.append(pp.heappop()[0])
    # # pp.delete(test2[-1])
    # print(poplist2,max_h.tracker,max_h.D,max_h.ar)
    # print(lt,pplist,pp.tracker,[pp.D[i][1] for i in pp.ar],[pp.D[i][0] for i in pp.ar])

    # 100 times for length(1000) heap
    # for _ in range(20):

    for j in range(10):
        test1 = random.sample(list(range(4000)),10)
        test2 = random.sample(list(range(2000)),10)
        test = sorted(list(zip(test1,test2)),reverse=True)
        if j%2:
            pp = max_heap()
            for i in range(10):
                pp.heappush(tuple([test1[i],test2[i]]))
        else:
            pp = []
            pp = max_heap(list(zip(test1,test2)))
        pplist = []
        while pp.ar:
            pplist.append(pp.heappop())
        # print(pplist,'\n',sorted(list(zip(test1,test2)),reverse= True))
        for k in range(10):
            # if pplist[j]!=test[j]:
            print(pplist[k],test[k])
        # print()




