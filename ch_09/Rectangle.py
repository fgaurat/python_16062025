class Rectangle:
    # Compteur d'objet (static)
    __cpt = 0
    
    def __init__(self,longueur=1,largeur=1):
        assert isinstance(longueur,int)
        assert isinstance(largeur,int)
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1

    @classmethod
    def buildFromStr(cls,s:str): 
        # longueur,largeur = [int(v) for v in s.split(";")]
        # r = cls(longueur,largeur)
        values = [int(v) for v in s.split(";")]
        r = cls(*values)
        return r

    @staticmethod
    def getCpt():
        return Rectangle.__cpt


    @property
    def longueur(self):
        """Getter de la Propriété longueur"""
        return self.__longueur
    @property
    def largeur(self):
        """Getter de la Propriété largeur"""
        return self.__largeur

    @longueur.setter
    def longueur(self,longueur):
        """Setter de la Propriété longueur"""
        assert longueur > 0
        self.__longueur = longueur

    @largeur.setter
    def largeur(self,largeur):
        """Setter de la Propriété largeur"""
        assert largeur > 0
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__largeur*self.__longueur


    def __eq__(self, value) -> bool:
        return self.__longueur == value.longueur and self.__largeur == value.largeur

    def __str__(self)->str:
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"

    def __int__(self)->int:
        return self.surface