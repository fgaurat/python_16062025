def old_mult2(values):
    r = []
    for v in values:
        r.append(v*2)

    return r


def mult2(i):
    return i*2

l = [10,20,30,40,50]



# r = mult2(l)
r = list(map(lambda i:i*2,l))
print(r) # [20,40,60,80,100]

