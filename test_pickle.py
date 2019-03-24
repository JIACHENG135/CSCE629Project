import pickle
a = {'a':'b'}
b = {'c':'d'}
with open('test.pickle', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([a,b], f)
f.close()
with open('test.pickle', 'rb') as f:  # Python 3: open(..., 'wb')
    c,d = pickle.load(f)
f.close()
print(c,d)