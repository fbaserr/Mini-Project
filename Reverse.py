l=[[1, 2], [3, 4], [5, 6, 7]]
l_rv=[]
def rev(x):
    for i in l:
        if type(i)==type([]):
            i.reverse()
            l_rv.append(i)

rev(l)
l_rv.reverse()
print(l_rv)
