import random
class min_heap(object):
    # build min heap
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
        if l<len(self.ar) and self.D[self.ar[l]]<self.D[self.ar[ind]]:
        # if l<self.size and self.D[self.ar[l]]>self.D[self.ar[ind]]:
            larg = l
        else:
            larg = ind
        if r<len(self.ar) and self.D[self.ar[r]]<self.D[self.ar[larg]]:
            larg = r
        if larg!=ind:
            self.tracker[self.D[self.ar[ind]][1]] = larg
            self.tracker[self.D[self.ar[larg]][1]] = ind
            self.ar[ind],self.ar[larg] = self.ar[larg],self.ar[ind]
            self.switch_down(larg)
    def switch_up(self,ind):
        if ind==0:return
        p = int((ind-1)/2)
        if self.D[self.ar[p]]>self.D[self.ar[ind]]:
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
        if self.D[self.ar[ind]]<self.D[self.ar[int((ind-1)/2)]]:
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
        # flag = True
        if 2*(ind+1)-1<len(self.ar):
            if self.D[self.ar[ind]]>self.D[self.ar[2*(ind+1)-1]]:
                return False
                # return 
                print('false',self.D[self.ar[ind]],self.D[self.ar[2*(ind+1)-1]])
            self.check(2*(ind+1)-1)
        if 2*(ind+1)<len(self.ar):
            if self.D[self.ar[ind]]>self.D[self.ar[2*(ind+1)]]:
                return False
                # return
                print('false',self.D[self.ar[ind]],self.D[self.ar[2*(ind+1)]])
            self.check(2*(ind+1))
        return True

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
                return False
            self.check(2*(ind+1)-1)
        if 2*(ind+1)<len(self.ar):
            if self.D[self.ar[ind]]<self.D[self.ar[2*(ind+1)]]:
                print('false',self.D[self.ar[ind]],self.D[self.ar[2*(ind+1)]])
                return False
            self.check(2*(ind+1))
        return True
            


if __name__ == '__main__':
    # general test for push pop and heapfy


    test1 = random.sample(list(range(4000)),10)
    test2 = random.sample(list(range(2000)),10)
    # test = sorted(list(zip(test1,test2)),reverse=True)# for max_heap test
    test = sorted(list(zip(test1,test2)))# for min_heap test
    




    # test for push
    
    # pp = max_heap()
    # pp = min_heap()
    # for i in range(1000):
    #     pp.heappush(tuple([test1[i],test2[i]]))

    # test for heapfy
    
    # pp = min_heap(list(zip(test1,test2)))
    


    # pplist = []
    # while pp.ar:
    #     pplist.append(pp.heappop())
    # res = []
    # for k in range(1000):
    #     res.append(pplist[k]!=test[k])
    # print(any(res))

    # test for delete
    for k in test2:
        print(k)
        minh = min_heap(list(zip(test1,test2)))
        print([minh.D[i] for i in minh.ar])
        if not minh.check(0):
            print('fail')
            # break
        minh.delete(k)
        print([minh.D[i] for i in minh.ar])
        if not minh.check(0):
            print('fail')
            # break



