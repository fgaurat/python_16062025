class Rectangle:

    def __init__(self,longueur,largeur):
        assert isinstance(longueur,int)
        assert isinstance(largeur,int)
        self.__longueur = longueur
        self.__largeur = largeur


    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    def setLongueur(self,longueur):
        assert longueur > 0
        self.__longueur = longueur

    def setLargeur(self,largeur):
        assert largeur > 0
        self.__largeur = largeur

    def getSurface(self):
        return self.__largeur*self.__longueur


    longueur = property(getLongueur,setLongueur,doc="Propriété longueur")
    largeur = property(getLargeur,setLargeur,doc="Propriété largeur")
    surface = property(getSurface,doc="Propriété surface")