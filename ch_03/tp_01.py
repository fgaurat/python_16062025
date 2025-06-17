import copy 

# Ceci est un commentaire
# Ceci est un commentaire
# Ceci est un commentaire


p = "c:\\test\\new_project"
print(p)
p = r"c:\test\new_project"
print(p)


multilines = """Ceci est une ligne
ceci est une autre ligne
et encore  une autre ligne.
"""

print(multilines)

a =2
s = "valeur de a:"+str(a)
print(s)

a =2
s = "valeur de a:"*a
print(s)
print(50*'#')
print("la suite")
print(50*'#')
word = 'Python'
print(word[0])
taille = len(word)
print(taille)
last = word[len(word)-1]
last = word[-1]

print(word[0:2]) #[0:2[
print(word[2:5]) #[2:5[
print(word[2:]) #[2:la_fin[
print(word[:]) #[2:la_fin[
print(len(word[:4876])) #[2:la_fin[


print(word)
# word[0] = 'J'
print(50*'#')
word = 'Python'
word1 = 'J'+word[1:]

print(hex(id(word)))
print(hex(id(word1)))

print("## Les Listes ##")
squares = [1, 4, 9, 16, 25]
print(squares)
squares[3] = 643
print(squares)
squares.append(36)
print(squares)

squares2 = squares
squares[0] = 1000
print(squares) 
print(squares2)

squares2 = squares[:] # shallow copy
# squares2 = squares.copy() # shallow copy
squares[0] = 1000
print(squares) 
print(squares2)

l = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
# l1 = l[:] # shallow copy
l1 = copy.deepcopy(l)
l[1][1] = 1000
print(l)
print(l1)
