from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    ce = Cercle(2)
    print(c.cote)
    print(c.surface)
    c.cote = 4
    # print(c.cote)
    print(c.surface)
    print(c)

    print(ce)
    print(ce.surface)
    print(c.surface)    

if __name__=='__main__':
    main()
