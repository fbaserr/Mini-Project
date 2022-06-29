def flatten(x):
    for i in x:
        if type(i)==type([]):
            flatten(i)
        else:
            l_fl.append(i)

l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l_fl=[]

flatten(l)
print(l_fl)