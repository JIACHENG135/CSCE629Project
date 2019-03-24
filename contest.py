def smallestRepunitDivByK(K):
    if K%2==0 or K%5==0:return -1
    if K==1:return 1
    rest =set()
    l = 2
    rem = 1
    # rest.add()
    s = 1
    # if K%5==0:return -1
    while s%K and s not in rest:
        l += 1
        rest.add(s)
        # rem = int('1'*l)%K
        rem = (10*rem)%K
        s += rem
    if s in rest:
        return -1
    if not s%K:
        return l-1
for i in range(100000):
    print(smallestRepunitDivByK(i))

