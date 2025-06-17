l = [10,20,30,40,50]


for v in l:
    print(v)

for i in range(len(l)) :
    print(i,l[i])

for pos,data in enumerate(l) :
    print(pos,data)



d = {"name":"GAURAT","firstName":"Fred","job":"dev","age":49}


for k in d:
    print(k, d[k])

for k,v in d.items():
    print(k,v)

# for k,v in enumerate(d):
#     print(k,v)


l = list(d)
keys = d.keys() 
values = d.values() 