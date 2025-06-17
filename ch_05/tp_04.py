d = {"name":"GAURAT","firstName":"Fred"}
print(d)
print(d['name'])
d['firstName'] = "Frédéric"
print(d)
d['languages'] = ["Python","PHP","Javascript"]
print(d)

for l in d['languages']:
    print(l)