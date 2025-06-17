l = ['Valeur 01','Valeur 02','Valeur 03','Valeur 04']


for the_value in l:
    print(the_value)

for i in range(5):
    print(i)

for i in range(len(l)):
    # print(str(i)+" "+l[i])
    print(i,l[i])


print(range(3))
print(list(range(3)))




l = [2,5,12,76,89,34]
to_find = 760

for i in l:
    print(i)
    if i == to_find:
        print("found")
        break
else:
    print("not found!")