import random
class min_heap(object):
    # build min heap
    def __init__(self,nums=[]):
        self.ar = nums
        self.size = len(nums)
        self.heapfy()
    def heapfy(self):
        for ind in range(self.size):
            if self.ar[ind]<self.ar[(ind-1)//2]:
                self.switch_up(ind)
    def left(self,ind):
        return 2*(ind+1)-1
    def right(self,ind):
        return 2*(ind+1)
    def switch_down(self,ind):
        l = self.left(ind)
        r = self.right(ind)
        if r<self.size and self.ar[r]<self.ar[ind]:
            larg = r
        else:
            larg = ind
        if l<self.size and self.ar[l]<self.ar[larg]:
            larg = l
        if larg!=ind:
            self.ar[ind],self.ar[larg] = self.ar[larg],self.ar[ind]
            self.switch_down(larg)
    def switch_up(self,ind):
        if ind==0:return
        p = int((ind-1)/2)
        if self.ar[p]>self.ar[ind]:
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
        if self.ar[ind]<self.ar[int((ind-1)/2)]:
            self.switch_up(ind)
        else:
            self.switch_down(ind)
    def heappush(self,num):
        self.ar.append(num)
        self.size += 1
        self.switch_up(self.size-1)

    def heappop(self):
        if not self.ar:
            print('pop from an empty heap')
            return
        minv = self.ar[0]
        self.ar[0] = self.ar[self.size-1]
        self.size -= 1
        self.switch_down(0)
        self.ar.pop()
        return minv
    def check(self,ind):
        if 2*(ind+1)-1<self.size:
            if not self.ar[ind]<=self.ar[2*(ind+1)-1]:
                print(self.ar,self.ar[ind],self.ar[2*(ind+1)-1])
            self.check(2*(ind+1)-1)
        if 2*(ind+1)<self.size:
            if not self.ar[ind]<=self.ar[2*(ind+1)]:
                print(self.ar[ind],self.ar[2*(ind+1)])
            self.check(2*(ind+1))
    




if __name__ == '__main__':
    # test = [6,2,3,45,75,12,26,13,24,1,4,2,4,9,1,2,4,6,1,2,2,16,11,4,23,47,8,745,741,3]
    test = random.sample(list(range(400)),30)



    # test for delete
    print(test)
    a = min_heap(test)
    print(a.ar)
    while a.ar:
        index = int((a.size-1)*random.random())
        a.delete(index)
        a.check(0)

    # test for push and pop
    a = min_heap()
    test = random.sample(list(range(400)),50)

    for i in test:
        a.heappush(i)
    poplist = []
    while a.ar:
        poplist.append(a.heappop())
    print(poplist,'\n',sorted(test))




