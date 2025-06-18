from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(3,6)
    r1 = DataRectangle(3,6)
    print(r1.surface)

    print(r.longueur)
    print(r.largeur)
    r.longueur = 45
    r.largeur=5
    print(r.longueur)
    print(r.largeur)
    print(r.surface)
    
    print(r)
    print(r1)
    print(50*'-')
    r = Rectangle(3,6)
    r1 = Rectangle(3,6)

    if r==r1:
        print("ok")
    else:
        print("ko")
    
    i = int(r)
    print(i)

    print(r.getCpt())
    print(r1.getCpt())
    print(Rectangle.getCpt())
    print(50*'-')
    r = Rectangle.buildFromStr("3;5")
    r1 = Rectangle(3,6)
    print(r)
def oldmain():
    r = Rectangle(3,6)
    print(r.getLongueur())
    print(r.getLargeur())

    r.setLongueur(2)
    print(r.getLongueur())
    print(r.getLargeur())

    # r.setLongueur(-12)

    print(r.getLongueur())
    print(r.getLargeur())

    print(r.getSurface())


    r.longueur =12
    print(r.longueur)

if __name__=='__main__':
    main()
