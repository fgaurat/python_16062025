
def add(*values):
    print(values)
    r = 0
    for i in values:
        r+=i
    return r

# def add(values):
#     return sum(values)


# l = [10,20,30,40,50]
# r = add(l)
# print(r) # 150

# r = add(10,20,30,40,50)

# # a,b = 0,1

a,b,*c = 0,1,2
print(a,b,c)
l = [10,20,30,40,50]
r = add(*l)
print(r)

print(l)# print([10,20,30,40,50])
print(*l,sep=",")# print(10,20,30,40,50,sep=",")


print(1,2)
print([1,2])

# a,b = (0,1)
# a,b = 0,1


# def hello(name,firstName):
def hello(**kwargs):
    print(kwargs)
    print("Bonjour", kwargs["firstName"], kwargs["name"], kwargs["job"], kwargs["age"] )
    # print("Bonjour",name,firstName)

# hello("GAURAT","Fred")
# hello(name="GAURAT",firstName="Fred")
hello(firstName="Fred", name="GAURAT",job="Dev",age=49)